import mysql.connector
from model.group import Group
from model.contact_properties import Contact_properties

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, phone2, notes, id FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, phone2, notes, id) = row
                list.append(Contact_properties(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company, address=address, home=home, mobile=mobile, work=work, fax=fax, email=email, email2=email2, email3=email3, homepage=homepage, byear=byear, ayear=ayear, address2=address2, phone2=phone2, notes=notes, id=id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()