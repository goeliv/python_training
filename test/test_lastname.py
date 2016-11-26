import re
from random import randrange

def test_lastname_on_home_page(app):
    contacts = app.contacts.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contacts.get_contact_list()[index]
    contact_from_edit_page = app.contacts.get_contact_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname