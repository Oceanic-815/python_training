from model.contact_properties import Contact_properties
from random import randrange

def test_edit_contact(app):
    old_contacts_list = app.contact.get_contact_list()
    cont_mod = Contact_properties(firstname="Edited!!!", middlename="Edited!!!", lastname="Edited!!!", nickname="JUST ADDED!", title="JUST ADDED!", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643", mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg", email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14", phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj")
    if app.contact.count_cont() == 0:
        app.contact.add_contact(cont_mod)
    index_cont = randrange(len(old_contacts_list))
    cont_mod.id = old_contacts_list[index_cont].id
    app.contact.edit_contact_by_index(index_cont)
    new_contacts_list = app.contact.get_contact_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[index_cont] = cont_mod
    assert sorted(old_contacts_list, key=Contact_properties.id_or_max) == sorted(new_contacts_list,
                                                                                     key=Contact_properties.id_or_max)