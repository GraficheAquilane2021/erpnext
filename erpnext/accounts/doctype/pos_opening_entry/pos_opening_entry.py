# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cint, get_link_to_form
from frappe.model.document import Document
from erpnext.controllers.status_updater import StatusUpdater

class POSOpeningEntry(StatusUpdater):
	def validate(self):
		self.validate_pos_profile_and_cashier()
		self.validate_payment_method_account()
		self.set_status()

	def validate_pos_profile_and_cashier(self):
		if self.company != frappe.db.get_value("POS Profile", self.pos_profile, "company"):
			frappe.throw(_("POS Profile {} does not belongs to company {}".format(self.pos_profile, self.company)))

		if not cint(frappe.db.get_value("User", self.user, "enabled")):
			frappe.throw(_("User {} has been disabled. Please select valid user/cashier".format(self.user)))
	
	def validate_payment_method_account(self):
		for d in self.balance_details:
			account = frappe.db.get_value("Mode of Payment Account", 
				{"parent": d.mode_of_payment, "company": self.company}, "default_account")
			if not account:
				frappe.throw(_("Please set default Cash or Bank account in Mode of Payment {0}")
					.format(get_link_to_form("Mode of Payment", mode_of_payment)), title=_("Missing Account"))

	def on_submit(self):
		self.set_status(update=True)