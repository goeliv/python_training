import re
from random import randrange

def test_emails_on_home_page(app):
    contacts = app.contacts.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contacts.get_contact_list()[index]
    contact_from_edit_page = app.contacts.get_contact_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                                 map(lambda x: clear (x), filter (lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

