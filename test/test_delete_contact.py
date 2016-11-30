from model.contact_properties import Contact_properties
import random

def test_delete_contact(app, db):
    if app.contact.count_cont() == 0:
        app.contact.add_contact(Contact_properties(firstname="JUST ADDED!", middlename="JUST ADDED!", lastname="JUST ADDED!", nickname="JUST ADDED!", title="JUST ADDED!", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643", mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg", email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14", phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj"))
    old_contacts_list = db.get_contact_list()
    contact = random.choice(old_contacts_list)
    #index_cont = randrange(len(old_contacts_list))
    app.contact.del_contact_by_id(contact.id)
    # new_contacts_list = db.get_contact_list()
    # assert len(old_contacts_list) - 1 == len(new_contacts_list)
    # #old_contacts_list[index_cont:index_cont+1] = []
    # old_contacts_list.remove(contact)
    # assert old_contacts_list == new_contacts_list