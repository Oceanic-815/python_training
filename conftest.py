import pytest
from fixture.application import Application
import json
import os.path

fixture = None # глобальные переменные:
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")  # получаем доступ к сохраненному параметру через объект request
    if target is None:
        # __file__ - var, содержащая путь к текущему файлу. Преобразуем его в абсолютный и присоединяем target.json.
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open (config_file) as f: # читаем файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser): # (hook) передается парсер командной строки
    parser.addoption("--browser", action="store", default="firefox") # параметр, действие сохранить, действие по умолчанию
    parser.addoption("--target", action="store", default="target.json")

