from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Rubrica"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Rubrica",
					"description": _("Rubrica clienti grafiche"),
					"onboard": 1,
				},
			]
		},		
	]
