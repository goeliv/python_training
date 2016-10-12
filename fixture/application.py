from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactsHelper
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Application:

    def __init__(self):
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        self.wd = WebDriver(firefox_binary=binary)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper (self)
        self.contacts = ContactsHelper (self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy (self):
        self.wd.quit()
