# Copyright 2015 Tecnativa - Antonio Espinosa
# Copyright 2016 Tecnativa - Sergio Teruel
# Copyright 2017 Tecnativa - David Vidal
# Copyright 2019 FactorLibre - Rodrigo Bonilla
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Optional validation of VAT via VIES",
    'category': 'Accounting',
    'version': '12.0.1.0.2',
    'depends': [
        'base_vat',
    ],
    'external_dependencies': {
        'python': ['stdnum'],
    },
    'data': [
        'views/res_partner_view.xml',
    ],
    'author': 'Tecnativa,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/account-financial-tools',
    'license': 'AGPL-3',
    'installable': True,
}
