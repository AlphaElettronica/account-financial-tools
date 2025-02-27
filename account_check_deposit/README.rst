=======================
Account Deposit in Bank
=======================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:7b77e339f675bbcc0f1611b45057eb237c9ff72a5015abe2391fd2471f2841d4
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Mature-brightgreen.png
    :target: https://odoo-community.org/page/development-status
    :alt: Mature
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--financial--tools-lightgray.png?logo=github
    :target: https://github.com/OCA/account-financial-tools/tree/12.0/account_check_deposit
    :alt: OCA/account-financial-tools
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-financial-tools-12-0/account-financial-tools-12-0-account_check_deposit
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-financial-tools&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows you to easily manage deposits : you can select all
the payment lines you received and create a global deposit for the selected
payments lines.
This module supports multi-currency ; each deposit has a currency and all the
lines of the deposit must have the same currency (so, if you have payments in
EUR and payments in USD, you must create 2 deposits: one in EUR and one in USD).

**Table of contents**

.. contents::
   :local:

Configuration
=============

In the menu *Invoicing > Configuration > Accounting > Journals*, create a new
journal:

* Name: Checks Received
* Type: Bank
* Short Code: CHK (or any code you want)
* Default Debit Account: select an account for checks received
* Default Credit Account: idem

This bank journal will be available as a payment method in Odoo. The account
you configured as *Default Debit Account* and *Defaut Credit Account* is the
account via which the amounts of checks will transit between the reception of a
check from a customer and the validation of the check deposit in Odoo.

On the Settings page of the Accounting, you should configure the
*Check Deposit Offsetting Account*:

* if you select *Bank Account*, the counter-part of the account move related to
  the check deposit will be the default debit account of the bank account
  selected on the check deposit.
* if you select *Transfer Account*, you will have to select a specific account
  that will be used as transfer account for check deposits.

Usage
=====

When you receive a check that pays a customer invoice, you can go to that
invoice and click on the button *Register Payment* and select the
*Check Received* journal as *Payment Journal*.

When you want to deposit checks to the bank, go to the menu
*Invoicing > Accounting > Check Deposit*, create a new check deposit and set the
journal *Checks Received* and select the bank account on which you want to
credit the checks. Then click on *Add a line* to select the checks you want to
deposit at the bank. Eventually, validate the deposit and print the report
(you probably want to customize this report).

Known issues / Roadmap
======================

* Add an option on journals that can be deposited ``grouped_move_line``
  to generate an account move with a single main line, that reconciles
  all the lines.

* Move the configuration ``check_deposit_offsetting_account`` and
  ``check_deposit_transfer_account_id`` from ``res.company`` to the
  ``account.journal`` that can be deposited.
  Make required the ``bank_journal_id`` field, only in the ``bank_account``
  option and not in the ``transfer_account`` option.

* Rename fields that belong ``check`` as this module allow to make deposit
  of checks, cash, etc...

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-financial-tools/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-financial-tools/issues/new?body=module:%20account_check_deposit%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion
* Tecnativa
* GRAP

Contributors
~~~~~~~~~~~~

* `Akretion <https://www.akretion.com>`_:

  * Benoît GUILLOT <benoit.guillot@akretion.com>
  * Chafique DELLI <chafique.delli@akretion.com>
  * Alexis de Lattre <alexis.delattre@akretion.com>
  * Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>

* `Tecnativa <https://www.tecnativa.com>`_:

  * Pedro M. Baeza

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/account-financial-tools <https://github.com/OCA/account-financial-tools/tree/12.0/account_check_deposit>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
