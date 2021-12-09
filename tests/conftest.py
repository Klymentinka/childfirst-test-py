import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
driver = None

REPORT_PATH = 'reports'


def pytest_addoption(parser):

    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "IE":
        print("IE driver")
        driver = webdriver.Ie(IEDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
