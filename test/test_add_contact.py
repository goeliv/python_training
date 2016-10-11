# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create(Contact(firstname="gkgk", middlename="gkgkg", lastname="gkhgkg", nick="gkgkgk", title="gkgk", company="gkgkjgkgk", address="gkgkjgkgk", home_tel="777", mob_tel="888",
                                work_tel="999", fax="777", email="2532@AMAI.COM", email2="2515832@AMAI.COM", homepage="ppp.com", birthday="1989"))
    app.session.logout()





