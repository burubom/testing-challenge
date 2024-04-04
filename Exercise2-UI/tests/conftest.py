import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():

    options = Options()
    options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size('1200', '1000')

    print('finish loading driver.')
    driver.get('https://www.debugbear.com/test/website-speed')

    yield driver

    print('driver closed.')
    driver.quit()


@pytest.fixture(autouse=True, scope='session')
def setup_print():
    print("\n")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


def pytest_html_report_title(report):
    report.title = "debugbear UI TEST"


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))


def pytest_html_results_table_row(report, cells):
    tmp_ele = ""
    for ele in report.description.splitlines():
        tmp_ele += ele + " \n"

    cells.insert(2, html.td(tmp_ele, style="white-space: pre-wrap; word-wrap: break-word;"))
