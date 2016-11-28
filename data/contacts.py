# -*- coding: utf-8 -*-
from model.contact_properties import Contact_properties
#import random
#import string


testdata = [
    Contact_properties(firstname="nameee1", middlename="middle name", lastname="last nameee1", nickname="nickname1",
                               title="jhfdjbjd", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643",
                               mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg",
                               email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14",
                               phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj"),
    Contact_properties(firstname="nameee2", middlename="middle name2", lastname="last nameee2", nickname="nickname2",
                               title="jhfdjbjd", company="kjjhjfgbkjd", address="dnfbghjdhbh, 123/32", home="65767834687643",
                               mobile="2376478476", work="3746539", fax="23343344", email="hggft@nfm.com", email2="dfghng@ghf.jg",
                               email3="swegf@hgbhf.bb", homepage="sdfgf.nbm.cn", byear="1555", ayear="1666", address2="hsgjdgjbs, 12/14",
                               phone2="1524152145", notes="fhgjhghsghvdvbbhghjfuefghyhrggfdv.,xj")
]

"""
def randomString(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*12
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact_properties(firstname=randomString("name", 10), middlename=randomString("middlename", 10), lastname=randomString("lastname", 10),
                       nickname=randomString("nick", 10), title=randomString("title", 10), company=randomString("company", 10),
                       address=randomString("address", 20), home=randomString("355455", 6), mobile=randomString("455335", 9),
                       work=randomString("24435", 6), fax=randomString("4334", 6), email=randomString("email@mail.ru", 4),
                       email2=randomString("email2@mail.ru", 4), email3=randomString("email3@mail.ru", 4), homepage=randomString("homepage.com", 4),
                       byear=randomString("1555", 2), ayear=randomString("1666", 2), address2="address", phone2=randomString("234332", 10),
                       notes=randomString("notes", 30))
    for i in range(5)
]
"""