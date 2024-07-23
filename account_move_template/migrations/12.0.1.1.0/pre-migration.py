from openupgradelib import openupgrade



def migrate_account_move_template(env):
    openupgrade.delete_records_safely_by_xml_id(env,
                                                ['account_move_template.view_account_move_form',
                                                 'account_move_template.account_move_template_form'], delete_childs=True)

    openupgrade.logged_query(env.cr, """
        UPDATE account_move
        SET ref = CONCAT('stipendi - ', COALESCE(ref, ''))
        WHERE account_move_template IS NOT NULL
    """)

    # Add new fields to account.move.template
    openupgrade.add_fields(env, [
        ('company_id', 'account.move.template', False, 'many2one', 'int4', 'base'),
        ('ref', 'account.move.template', False, 'char', 'varchar', 'base'),
        ('active', 'account.move.template', False, 'boolean', 'bool', 'base'),
    ])

    # Rename fields in account.move.template
    openupgrade.rename_fields(env, [
        ('account.move.template', 'account_move_template', 'account_journal_id', 'journal_id'),
        ('account.move.template', 'account_move_template', 'move_line_ids', 'line_ids'),
    ])

    # Add new fields to account.move.template.line
    openupgrade.add_fields(env, [
        ('sequence', 'account.move.template.line', False, 'integer', 'int4', 'base'),
        ('partner_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
        ('analytic_account_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
        ('analytic_tag_ids', 'account.move.template.line', False, 'many2many', 'int4', 'base'),
        ('tax_ids', 'account.move.template.line', False, 'many2many', 'int4', 'base'),
        ('tax_line_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
        ('company_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
        ('company_currency_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
        ('note', 'account.move.template.line', False, 'char', 'varchar', 'base'),
        ('type', 'account.move.template.line', False, 'selection', 'varchar', 'base'),
        ('python_code', 'account.move.template.line', False, 'text', 'text', 'base'),
        ('move_line_type', 'account.move.template.line', False, 'selection', 'varchar', 'base'),
        ('payment_term_id', 'account.move.template.line', False, 'many2one', 'int4', 'base'),
    ])

    # Rename fields in account.move.template.line
    openupgrade.rename_fields(env, [
        ('account.move.template.line', 'account_move_template_line', 'account_template_id', 'template_id'),
    ])

    # Set increasing sequence for account.move.template.line
    openupgrade.logged_query(env.cr, """
        WITH cte AS (
            SELECT id, ROW_NUMBER() OVER (PARTITION BY template_id ORDER BY id) - 1 as row_num
            FROM account_move_template_line
        )
        UPDATE account_move_template_line aml
        SET sequence = cte.row_num
        FROM cte
        WHERE aml.id = cte.id
    """)

    openupgrade.logged_query(env.cr, """
        UPDATE account_move_template_line
        SET move_line_type = CASE
            WHEN is_debit THEN 'dr'
            WHEN is_credit THEN 'cr'
            ELSE 'dr'  -- Default to debit if neither is set
        END
    """)

    # Drop old fields
    openupgrade.drop_columns(env.cr, [
        ('account_move_template_line', 'is_debit'),
        ('account_move_template_line', 'is_credit'),
    ])


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return
    migrate_account_move_template(env)
