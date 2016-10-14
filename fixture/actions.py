"""
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.session_cont import Session_contHelper

class Actions:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.contact = ContactHelper(self)
        self.session_cont = Session_contHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
"""