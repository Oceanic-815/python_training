# -*- coding: utf-8 -*-
import unittest

from fixture.actions import Actions
from model.contact_properties import Contact_properties


class test_add_new_contact(unittest.TestCase):
    def setUp(self):
        self.act = Actions()

    def test_add_new_contact(self):
        self.act.login(username="admin", password="secret")
        self.act.contact.add_contact(Contact_properties(firstname="nameee1", middlename="middle name", lastname="last nameee1", nickname="nickname1", title="jhfdjbjd", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643", mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg", email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14", phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj"))
        self.act.logout()

    def tearDown(self):
        self.act.destroy()

if __name__ == '__main__':
    unittest.main()
