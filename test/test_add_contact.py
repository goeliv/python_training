

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact=Contact(firstname="new", middlename="new", lastname="new", nick="new", title="new", company="new", address="new", home_tel="new", mob_tel="new",
                                work_tel="new", fax="new", email="new@AMAI.COM", email2="new@AMAI.COM", homepage="newppp.com", birthday="1900")
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



