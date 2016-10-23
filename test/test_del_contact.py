from model.contact import Contact


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test", middlename="test", lastname="gkhgkg", nick="gkgkgk", title="gkgk", company="gkgkjgkgk", address="gkgkjgkgk", home_tel="777", mob_tel="888",
                                work_tel="999", fax="777", email="2532@AMAI.COM", email2="2515832@AMAI.COM", homepage="ppp.com", birthday="1989"))
        old_contacts = app.contacts.get_contact_list()
        app.contacts.delete_first_contact()
        new_contacts = app.contacts.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)