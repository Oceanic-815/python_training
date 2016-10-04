# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    #success = True
    app.login(username="admin", password="secret")
    app.create_group(Group(name="3333", header="3333", footer="3333"))
    app.logout()

#***>> added manually to check behaviour with empty fields <<***
def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
