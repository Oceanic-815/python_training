# -*- coding: utf-8 -*-
from model.contact_properties import Contact_properties

def test_add_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts_list = db.get_contact_list()
    app.contact.add_contact(contact)
    new_contacts_list = db.get_contact_list()
    #assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact_properties.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact_properties.id_or_max)
