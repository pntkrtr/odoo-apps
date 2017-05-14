# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
##############################################################################
#
# SGE04_Tarea: Víctor Manuel Espinosa López
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Citas',
	'version': '1.0',
	'author': "Victor Manuel Espinosa López",
	'website': "http://www.victorespinosasoftware.es",
	# Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'summary': 'Almacenamiento de citas y autores',
    'description': """
Este módulo permite almacenar citas, sus autores y la fecha.
Si en la misma fecha hay varias citas podemos establecer un orden de presentación.
""",
	# any module necessary for this one to work correctly
    'depends': ['base'],
	# always loaded
    'data': [
		# 'security/ir.model.access.csv',
		# 'views/citasvmel_views.xml',
		'views/views.xml',
		'views/templates.xml',
    ],
	# only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'installable': True,
    'application': True,
	'auto_install': False,
}