from model.contact_properties import Contact_properties

def test_edit_contact(app):
    if app.contact.count_cont() == 0:
        app.contact.add_contact(Contact_properties(firstname="JUST ADDED!", middlename="JUST ADDED!", lastname="JUST ADDED!", nickname="JUST ADDED!", title="JUST ADDED!", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643", mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg", email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14", phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj"))
    app.contact.edit_contact()