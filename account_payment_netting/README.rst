=======================
Account Payment Netting
=======================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:7c8b381fe83dbd3355b2517c5c066b7714ff2ece1aa4e720171680f9769d34e7
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--financial--tools-lightgray.png?logo=github
    :target: https://github.com/OCA/account-financial-tools/tree/12.0/account_payment_netting
    :alt: OCA/account-financial-tools
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-financial-tools-12-0/account-financial-tools-12-0-account_payment_netting
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-financial-tools&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allow net payment on AR/AP invoice from the same business partner.

**NOTE**: This module is influenced by account_netting,
but make it more user friendly when netting invoices.
While account netting require user to select manually the journal items to do netting
(which create netting journal entry), this module has a new menu "Invoices to netting"
allowing user to select both customer/supplier invoice to register payment.

**Table of contents**

.. contents::
   :local:

Usage
=====

Given there are open invoices both receivable and payable,
and user decide to make payment on the diff.

- Open menu Accounting > Invoices to Netting
- Select multiple open invoices from the same partner
- Click on action "Register Payment", the wizard will show the diff amount
- Make payment as normal

This create Customer Payment if AR > AP, Supplier Payment otherwise.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-financial-tools/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-financial-tools/issues/new?body=module:%20account_payment_netting%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Ecosoft

Contributors
~~~~~~~~~~~~

* Kitti Upariphutthiphong <kittiu@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-kittiu| image:: https://github.com/kittiu.png?size=40px
    :target: https://github.com/kittiu
    :alt: kittiu

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-kittiu| 

This module is part of the `OCA/account-financial-tools <https://github.com/OCA/account-financial-tools/tree/12.0/account_payment_netting>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
