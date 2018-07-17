# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Nicolas Bornand
#
#    The licence is in the file __manifest__.py
#
##############################################################################
import logging
from odoo.addons.sponsorship_compassion.tests.test_sponsorship_compassion\
    import BaseSponsorshipTest
from odoo import fields
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class TestAnalyticAttribution(BaseSponsorshipTest):

    def setUp(self):
        super(TestAnalyticAttribution, self).setUp()
        self.child = self.create_child('UG1119182')
        self.rule = self.env.ref('sms_sponsorship.release_booking_by_sms_rule')

    def test_book_by_sms__and_eviction_rule(self):
        hold = self.child.hold_id
        self.assertFalse(hold.booked_by_phone_number)
        hold.book_by_sms('021 345 67 89')
        self.assertTrue(hold.booked_by_phone_number)

        hold.booked_at = fields.Datetime.from_string('2018-01-01')
        self.rule._check()
        self.assertFalse(hold.booked_by_phone_number)
        self.assertFalse(hold.booked_at)

    def test_book_by_sms__should_fail_if_already_booked(self):
        hold = self.child.hold_id
        self.assertFalse(hold.booked_by_phone_number)
        hold.book_by_sms('021 345 67 89')
        with self.assertRaises(UserError):
            hold.book_by_sms('023 345 67 89')
