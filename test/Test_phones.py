

def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_tel ==contact_from_edit_page.home_tel
    assert contact_from_home_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_home_page.mob_tel == contact_from_edit_page.mob_tel
    assert contact_from_home_page.secondary_tel == contact_from_edit_page.secondary_tel