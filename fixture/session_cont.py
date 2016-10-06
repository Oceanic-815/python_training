class Session_contHelper:
    def __init__(self, app_cont):
        self.app_cont = app_cont

    def login(self, username, password):
        wd = self.app_cont.wd
        self.app_cont.open_home_page()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app_cont.wd
        wd.find_element_by_link_text("Logout").click()
