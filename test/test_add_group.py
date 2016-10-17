# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group



def test_add_group(app):
    app.group.create(Group(name="dfgdfg", header="dfgdfgd", footer="dfgdfgdfg"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



