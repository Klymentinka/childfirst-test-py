import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.mongodb import MongoDB


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()

def pytest_bdd_before_scenario(request, feature, scenario):
    mongodb = MongoDB()
    mongodb.clean_test_parents()
