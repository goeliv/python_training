import re
from random import randrange

def test_phones_on_home_page(app):
    contacts = app.contacts.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contacts.get_contact_list()[index]
    contact_from_edit_page = app.contacts.get_contact_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contacts.get_contact_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_from_edit_page(0)
    assert clear(contact_from_view_page.home_tel) == clear(contact_from_edit_page.home_tel)
    assert clear(contact_from_view_page.work_tel) == clear(contact_from_edit_page.work_tel)
    assert clear(contact_from_view_page.mob_tel) == clear(contact_from_edit_page.mob_tel)
    assert clear(contact_from_view_page.secondary_tel) == clear(contact_from_edit_page.secondary_tel)


def clear(s):
    re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                                 map(lambda x: clear (x), filter (lambda x: x is not None, [contact.home_tel, contact.work_tel, contact.mob_tel, contact.secondary_tel]))))

