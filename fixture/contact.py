from model.contact_properties import Contact_properties
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, contact_properties):
        wd = self.app.wd
            # open "Add new contact" page
        wd.find_element_by_link_text("add new").click()
            # enter a first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_properties.firstname)
            # enter a middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_properties.middlename)
            # enter last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_properties.lastname)
            # enter a nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_properties.nickname)
            # enter title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_properties.title)
            # enter company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_properties.company)
            # enter address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_properties.address)
            # enter home phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_properties.home)
            # enter mobile phone number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_properties.mobile)
            # enter work phone number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_properties.work)
            # enter a faz number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_properties.fax)
            # enter the first email address
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_properties.email)
            # enter the second email address
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact_properties.email2)
            # enter the third email address
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact_properties.email3)
            # enter a homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact_properties.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()
            # enter the birthday date
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_properties.byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()
            # enter another date
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_properties.ayear)
            # enter the second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_properties.address2)
            # enter the second phone number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_properties.phone2)
            # enter notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_properties.notes)
            #saving contact
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home").click()
            # Clean up cache
        self.contact_cache = None

    def edit_contact(self):
        self.edit_contact_by_index(0)
        self.contact_cache = None

    def edit_contact_by_index(self, index_cont):
        wd = self.app.wd
        # open contacts page if this page is still not open. Else - start editing contact
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()
        rowList = wd.find_elements_by_name("entry")[index_cont]
        cellsList = rowList.find_elements_by_tag_name("td") # создаем список ячеек в строке
        selectCell =  cellsList[7] # присваиваем переменной восьмую ячейку
        selectCell.find_element_by_tag_name("a").click()
            # Editing contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Edited!!!")
            # enter a middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Edited!!!")
            # enter last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Edited!!!")
            # enter a nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Edited!!!")
            # enter title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Edited!!!")
            # enter company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Edited!!!")
            # enter address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Edited!!!")
            # enter home phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("100000")
            # enter mobile phone number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("111111")
            # enter work phone number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("222222")
            # enter a faz number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("333333")
            # enter the first email address
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("Edited!!!@fgh.com")
            # enter the second email address
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("Edited!!!@edited.com")
            # enter the third email address
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("Edited!!!@fff.cv")
            # enter a homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("Edited!!!.edit.ed")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()
            # enter the birthday date
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("Edited!!!")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()
            # enter another date
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("Edited!!!")
            # enter the second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Edited!!!")
            # enter the second phone number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("444444")
            # enter notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Edited!!!")
            #saving contact
        wd.find_element_by_name("update").click()
        # Clean up cache
        self.contact_cache = None

    def del_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index_cont):
        wd = self.app.wd
        # open contacts page if this page is still not open. Else - start deleting contact
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()
         # select the first contact from the list
        wd.find_elements_by_name("selected[]")[index_cont].click()
         # contact deletion begins
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        # Clean up cache
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

        # define if there is any contact in the contacts list
    def count_cont(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

        # Сравниваем список контактов до и после добавления/удаления/модификации групп
    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")  # записываем в переменную атрибут "value" чек бокса
                cellsList = element.find_elements_by_tag_name("td")  # присваиваем переменной cellsList список элементов с именем тэга "td" - все ячейки строки
                lastNameCell = cellsList[1] # присваиваем переменной второй элемент в списке - ячейку с фамилией
                firstNameCell = cellsList[2] # ячейка с именем
                textFromLastName = lastNameCell.text # получаем текст из ячейки с фамилией
                textFromFirstName = firstNameCell.text  # получаем текст из ячейки с именем
                addressCell = cellsList[3].text
                allEmails = cellsList[4].text
                all_phones = cellsList[5].text # из ячейки 5 берем text
                self.contact_cache.append(Contact_properties(lastname=textFromLastName, firstname=textFromFirstName,
                                                             id=id, address=addressCell, allEmails_from_home_page=allEmails,
                                                             all_phones_from_home_page=all_phones))  # добавляем имя, фамилию и id в список контактов, а также телефоны
        return list(self.contact_cache)

    # открыть контакт для радактирования по индексу чтобы считать информацию с полей для метода get_contact_info_from_edit_page
    def open_contact_edit_page_by_index(self, index_cont):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()
        rowList = wd.find_elements_by_name("entry")[index_cont]
        selectCell = rowList.find_elements_by_tag_name("td")[7]
        selectCell.find_element_by_tag_name("a").click()

    # открыть страницу контакта по индексу
    def open_contact_view_page_by_index(self, index_cont):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")) and len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()
        rowList = wd.find_elements_by_name("entry")[index_cont]
        selectCell = rowList.find_elements_by_tag_name("td")[6]
        selectCell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index_cont):
        self.open_contact_edit_page_by_index(index_cont)
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        wd.find_element_by_link_text("home").click()
        # Из полученных данных строим объект (название_параметра = название_локальной_переменной)
        return Contact_properties(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile,
                                  phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index_cont):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index_cont)
        text = wd.find_element_by_id("content").text # получаем текст со страницы просмотра контакта
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        wd.find_element_by_link_text("home").click()
        return Contact_properties(home=homephone, work=workphone, mobile=mobilephone,
                                  phone2=secondaryphone)
