# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_new_contact(self):
        wd = self.wd
        # login
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # open "Add new contact" page
        wd.find_element_by_link_text("add new").click()
        # enter a first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("nameee1")
        # enter a middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("middle name")
        # enter last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("last nameee1")
        # enter a nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nickname1")
        # enter title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("jhfdjbjd")
        # enter company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("kjjhjfgbkjd")
        # enter address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("dnfbghjdhbh, 123/32")
        # enter home phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("65767834687643")
        # enter mobile phone number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("2376478476")
        # enter work phone number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("3746539")
        # enter a faz number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("23343344")
        # enter the first email address
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("hggft@nfm.com")
        # enter the second email address
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("dfghng@ghf.jg")
        wd.find_element_by_name("theform").click()
        # enter the third email address
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("swegf@hgbhf.bb")
        # enter a homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("sdfgf.nbm.cn")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[5]").click()
        # enter the birthday date
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1555")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()
        # enter another date
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1666")
        # enter the second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("hgsdjfhgbbfjbg,23/22")
        # enter the second phone number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("ghdghghghsgf")
        # enter notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("ggfsdhhgjhsdjbjhjhdgfjbhhjhjoiwpqowriueu")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
