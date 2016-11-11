import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contacts.get_contact_form_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_view_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_view_page.mob_tel == contact_from_edit_page.mob_tel
    assert contact_from_view_page.secondary_tel == contact_from_edit_page.secondary_tel


def clear(s):
    re.sub("[()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                                 map(lambda x: clear (x), filter (lambda x: x is not None, [contact.home_tel, contact.work_tel, contact.mob_tel, contact.secondary_tel]))))

