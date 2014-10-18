# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 Coop. Trab. Moldeo Interactive Ltda.
# http://business.moldeo.coop
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
{   'active': False,
    'author': 'Coop. Trab. Moldeo Interactive Ltda.',
    'category': 'Tools/Cryptography',
    'demo_xml': [],
    'depends': [],
    'description': '\nCryptography Manager can generate key pairs and certificates to connect to\n\n    other services.\n\n',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Cryptography Manager',
    'test': ['test/test_pairkey.yml', 'test/test_certificate.yml'],
    'update_xml': [   'crypto_menuitems.xml',
                      'security/crypto_security.xml',
                      'security/ir.model.access.csv',
                      'wizard/generate_pairkey.xml',
                      'wizard/generate_certificate.xml',
                      'wizard/generate_certificate_request.xml',
                      'pairkey_view.xml',
                      'certificate_view.xml'],
    'version': '0.3',
    'website': 'http://business.moldeo.coop'}
