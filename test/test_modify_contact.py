from model.contact import Contact


def test_modify_first_contact(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.modify(Contact(firstname="new", middlename="new", lastname="new", nick="new", title="new", company="new", address="new", home_tel="new", mob_tel="new",
                                work_tel="new", fax="new", email="new@AMAI.COM", email2="new@AMAI.COM", homepage="newppp.com", birthday="1900"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)