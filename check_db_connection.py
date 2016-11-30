import pymysql.cursors
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:

    l = orm.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass