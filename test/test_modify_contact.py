from model.contact import Contact
from random import randrange


def test_modify_some_contact(app, check_ui):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test", middlename="test", lastname="gkhgkg", nick="gkgkgk", title="gkgk",
                                    company="gkgkjgkgk", address="gkgkjgkgk", home_tel="777", mob_tel="888",
                                    work_tel="999", fax="777", email="2532@AMAI.COM", email2="2515832@AMAI.COM",
                                    homepage="ppp.com", birthday="1989"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="newf", middlename="newm", lastname="newl", nick="new", title="newt", company="newc", address="new", home_tel="111", mob_tel="222",
                                work_tel="333", fax="444", email="new@AMAI.COM", email2="new@AMAI.COM", homepage="newppp.com", birthday="1900")
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index,contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    #assert old_contacts == new_contacts
    #if check_ui:
        #assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     #key=Contact.id_or_max)
