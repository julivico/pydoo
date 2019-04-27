# -*- coding: utf-8 -*-

import pprint
from unittest import TestCase
from unittest import main as unittest_main

from pydoo import Odoo

pp = pprint.PrettyPrinter(indent=4)


class TestOdooConnector(TestCase):
    def setUp(self):
        self.odoo = Odoo(url="https://office.grimm-gastrobedarf.de",
                         db="produktion",
                         username="admin",
                         password="nmQd&5VD5P?!eLuB<djU",
                         use_ssl=True)

    def test_search_method(self):
        partner = self.odoo.env['res.partner']
        ret = partner.search([('customer', '=', True)])
        print("results of search method: " + str(ret))

    def test_search_method_with_pagination(self):
        partner = self.odoo.env['res.partner']
        ret = partner.search([['customer', '=', True]],
                             offset=5, limit=5)
        print("results of search method with pagination: " + str(ret))

    def test_search_read_records(self):
        partner = self.odoo.env['res.partner']
        ret = partner.search_read([('name', '=', 'GEV')])
        pp.pprint(ret)

    def test_fields_get(self):
        partner = self.odoo.env['res.partner']
        ret = partner.fields_get(fields=['name', 'customer', 'supplier'])
        print(ret)

    def test_create_partner(self):
        partner = self.odoo.env['res.partner']
        partner_id = partner.create(name="New partner 1234",
                                    type="contact")
        print("created partner with id: {}".format(partner_id))

    def test_write_partner(self):
        partner = self.odoo.env['res.partner']
        partner_ids = partner.search([['name', '=', 'New partner 1234']])
        print("found partner with ids: {}".format(partner_ids))
        result = partner.write(*partner_ids, name='New Partner 12345')
        print("changed partner result {}".format(result))

    def test_unlink_partner(self):
        partner = self.odoo.env['res.partner']
        partner_ids = partner.search([['name', '=', 'New Partner 12345']])
        print("found partner with ids: {}".format(partner_ids))
        result = partner.unlink(*partner_ids)
        print("unlink partner result {}".format(result))

    def test_unlink_magento_product_product(self):
        partner = self.odoo.env['magento.product.product']
        keys = [14586, 15858, 16075, 16546]
        result = partner.unlink(*keys)
        print("unlink products result {}".format(result))


if __name__ == '__main__':
    unittest_main()
