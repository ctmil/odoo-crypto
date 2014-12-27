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

class generate_pairkey(osv.osv_memory):
        _name = 'crypto.generate_pairkey'

        _columns = {
            'name': fields.char('Pair key name', size=63),
            'key_length': fields.integer('Key lenght'),
            'update': fields.boolean('Update key'),
        }

        _defaults = {
            'key_length': 1024,
        }

        def on_generate(self, cr, uid, ids, context):
            if context is None:
                context = {}
            active_ids = context['active_ids']
            pairkey_obj = self.pool.get('crypto.pairkey')
            for wizard in self.browse(cr, uid, ids):
                pairkey_obj.generate_keys(cr, uid, active_ids, key_length=wizard.key_length)
                pairkey_obj.action_validate(cr, uid, active_ids)
            return {'type': 'ir.actions.act_window_close'}

        def on_cancel(self, cr, uid, ids, context):
            return {}

generate_pairkey()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
