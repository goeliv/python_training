from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create(Contact(firstname="test", middlename="test", lastname="gkhgkg", nick="gkgkgk", title="gkgk", company="gkgkjgkgk", address="gkgkjgkgk", home_tel="777", mob_tel="888",
                                work_tel="999", fax="777", email="2532@AMAI.COM", email2="2515832@AMAI.COM", homepage="ppp.com", birthday="1989"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)