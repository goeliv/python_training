# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string1(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                    nick=random_string("nick", 20), title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 20),
                    home_tel=random_string1("home_tel", 20),  mob_tel=random_string1("mob_tel", 20),  work_tel=random_string1("work_tel", 20),  fax=random_string1("fax", 20),
                    email=random_string("email", 20), email2=random_string("email", 20), homepage=random_string("homepage", 20), birthday=random_string("birthday", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



