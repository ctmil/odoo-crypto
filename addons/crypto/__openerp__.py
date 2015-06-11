# -*- coding: utf-8 -*-
{'active': False,
 'author': 'Coop. Trab. Moldeo Interactive Ltda.',
 'category': 'Tools/Cryptography',
 'demo_xml': [],
 'depends': [],
 'description': '''
 Cryptography Manager can generate key pairs and certificates to connect to
 other services.
 ''',
 'init_xml': [],
 'installable': True,
 'license': 'AGPL-3',
 'name': 'Cryptography Manager',
 'test': ['test/test_pairkey.yml', 'test/test_certificate.yml'],
 'data': ['crypto_menuitems.xml',
          'security/crypto_security.xml',
          'security/ir.model.access.csv',
          'wizard/generate_pairkey.xml',
          'wizard/generate_certificate.xml',
          'wizard/generate_certificate_request.xml',
          'pairkey_view.xml',
          'certificate_view.xml'],
 'external_dependencies': {
     'python': ['M2Crypto'],
 },
 'version': '0.3',
 'website': 'http://business.moldeo.coop'}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
