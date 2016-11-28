# -*- coding: utf-8 -*-
from model.contact_properties import Contact_properties
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
