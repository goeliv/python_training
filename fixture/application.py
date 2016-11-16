from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactsHelper
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            self.wd = webdriver.Firefox(firefox_binary=binary)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper (self)
        self.contacts = ContactsHelper (self)
        self.base_url = base_url

    def is_valid (self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy (self):
        self.wd.quit()
