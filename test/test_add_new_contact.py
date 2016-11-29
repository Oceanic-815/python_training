# -*- coding: utf-8 -*-
from model.contact_properties import Contact_properties

def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_contacts_list = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(contact)
    assert sorted(old_contacts_list, key=Contact_properties.id_or_max) == sorted(new_contacts_list, key=Contact_properties.id_or_max)
