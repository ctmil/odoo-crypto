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

from openerp.osv import fields,osv
from openerp.tools.translate import _
from M2Crypto import X509
from datetime import datetime, timedelta

class generate_certificate(osv.osv_memory):
    _name = 'crypto.generate_certificate'

    def _get_partner_id(self, cr, uid, context={}):
        res = self.pool.get('res.users').read(cr, uid, [uid], ['partner_id'], context=context)
        if res and res[0]['partner_id']:
            return res[0]['partner_id'][0]
        return False

    _columns = {
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'serial_number': fields.integer('Serial number'),
        'version': fields.integer('Version'),
        'date_begin': fields.date('Begin date'),
        'date_end': fields.date('Expiration date'),
        'name_c':  fields.char('Country (C)', size=2),
        'name_sp': fields.char('State or Province Name (ST/SP)', size=64),
        'name_l':  fields.char('Locality Name (L)', size=64),
        'name_o':  fields.char('Organization Name (O)', size=64),
        'name_ou': fields.char('Organization Unit Name (OU)', size=64),
        'name_cn': fields.char('Common name (CN)', size=64),
        'name_gn': fields.char('Given Name (GN)', size=64),
        'name_sn': fields.char('Surname (SN)', size=64),
        'name_email': fields.char('E-mail Addres (EMail)', size=64),
        'name_serialnumber': fields.char('Serial Number (serialNumber)', size=64),
    }

    _defaults = {
        'partner_id': _get_partner_id,
        'serial_number': 1,
        'version': 2,
        'date_begin': (datetime.today() + timedelta(days=(0))).strftime('%Y-%m-%d'),
        'date_end': (datetime.today() + timedelta(days=(365))).strftime('%Y-%m-%d'),
    }

    def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
        v={}
        if partner_id:
            partner=self.pool.get('res.partner').browse(cr,uid,partner_id)
            try:
                v['name_c'] = partner.country_id.code
                v['name_sp'] = partner.state_id.name
                v['name_l'] = partner.city
                v['name_o'] = partner.name
                v['name_cn'] = partner.name
                v['name_email'] = partner.email
                # The following attributes are not set
                #v['name_ou'] = ''
                #v['name_gn'] = ''
                #v['name_sn'] = ''
                #v['name_serialnumber'] = ''
            except:
                pass
        return {'value': v }


    def on_generate(self, cr, uid, ids, context):
        if context is None:
            context = {}
        active_ids = context['active_ids']
        certificate_obj = self.pool.get('crypto.certificate')
        r_ids = []
        for wizard in self.browse(cr, uid, ids):
            name = X509.X509_Name()
            if wizard.name_c:  name.C  = wizard.name_c
            if wizard.name_sp: name.SP = wizard.name_sp
            if wizard.name_l:  name.L  = wizard.name_l
            if wizard.name_o:  name.O  = wizard.name_o
            if wizard.name_ou: name.OU = wizard.name_ou
            if wizard.name_cn: name.CN = wizard.name_cn
            if wizard.name_gn: name.GN = wizard.name_gn
            if wizard.name_sn: name.SN = wizard.name_sn
            if wizard.name_email: name.EMail = wizard.name_email
            if wizard.name_serialnumber: name.serialNumber = wizard.name_serialnumber
            r = certificate_obj.generate_certificate(cr, uid, active_ids,
                                                name, ext=None,
                                                serial_number=wizard.serial_number,
                                                version=wizard.version,
                                                date_begin=datetime.strptime(wizard.date_begin, '%Y-%m-%d'),
                                                date_end=datetime.strptime(wizard.date_end, '%Y-%m-%d'))
            r_ids.extend([ r[_id] for _id in active_ids ])
            certificate_obj.action_validate(cr, uid, active_ids)
        res_id = r_ids[0]
        return {
            'name': _('Request Certificate'),
            'res_model': 'crypto.certificate',
            'res_id': res_id,
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'form',
            'limit': 80,
        }

    def on_cancel(self, cr, uid, ids, context):
        return {}

generate_certificate()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
