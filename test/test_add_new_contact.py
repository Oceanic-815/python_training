# -*- coding: utf-8 -*-
from model.contact_properties import Contact_properties

def test_add_new_contact(app):
    old_contacts_list = app.contact.get_contact_list()
    cont = Contact_properties(firstname="nameee1", middlename="middle name", lastname="last nameee1", nickname="nickname1", title="jhfdjbjd", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643", mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg", email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14", phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj")
    app.contact.add_contact(cont)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list) # test fails here!
    old_contacts_list.append(cont)
    assert sorted(old_contacts_list, key=Contact_properties.id_or_max) == sorted(new_contacts_list, key=Contact_properties.id_or_max)