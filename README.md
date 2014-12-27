# Odoo-crypto

## Introduction

This addons let you manage key pairs and certificate used, in general, to access to remote services. This module was developed to connect Odoo to webservice of the Argentine Federal Administration of Public Revenue (AFIP).

## Description

This module is an interface to the M2Crypto library and its main objective is to manage cryptology objects in the Odoo interface. These objects will be used to encrypt or sign messages to other applications, for instance tax institutions.

It creates a new menu option in the Configuration menu, named Cryptography. This menu contains two menu items: Key pairs and Certificates. You can create key pairs in the interface and share it with other users in other systems. From those key pairs, you can create certificate requests. New certificate requests are stored in certificate objects. In these objects, you can generate a new certificate from a request, or associate a signed certificate to the request. The latter is the usual use of certificate requests.

Other modules can use these certificates and keypairs to sign or encrypt/decrypt messages between users in openerp or outside opener.

