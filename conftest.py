import pytest
from fixture.application import Application
from fixture.actions import Actions

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app_cont(request):
    fixture = Actions()
    request.addfinalizer(fixture.destroy)
    return fixture


