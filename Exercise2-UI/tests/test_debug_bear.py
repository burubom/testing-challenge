import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *
from conftest import driver


def test_mobile(driver):
    """
    Test Scenario: Enter the URL to initiate a speed test, choose 'mobile + EU East' as the configuration, and click the 'Start Test' button.
    Expectation: The speed test is executed. Following the advertisement display, the user is directed to the result page, where the selected device/region, target URL, and scores are displayed.
    """

    print('001 mobile test')
    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys(TARGET_URL)
    device_dropdown = driver.find_element(By.XPATH, DEVICE_DROPDOWN_XPATH)
    select = Select(device_dropdown)
    select.select_by_index(0)

    driver.find_element(By.XPATH, START_BTN_XPATH).click()
    print('waiting for the result...')

    testing_label = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, TESTING_LABEL_XPATH)))
    assert testing_label.text == 'Testing ' + TARGET_URL

    skip_link = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, SKIP_LINK_XPATH)))
    skip_link.click()

    assert driver.find_element(By.XPATH, URL_TEXT_XPATH).text == TARGET_URL.replace('https://', '')
    assert driver.find_element(By.XPATH, REGION_TEXT_XPATH).text == 'US EAST'
    assert driver.find_element(By.XPATH, DEVICE_TEXT_XPATH).text == 'MOBILE FAST'
    assert len(driver.find_elements(By.CLASS_NAME, SCORE_CLASS)) == 2
    for score_element in driver.find_elements(By.CLASS_NAME, SCORE_CLASS):
        assert re.match(r'\d{2}\%', score_element.text)


def test_desktop(driver):
    """
    Test Scenario: Enter the URL to initiate a speed test, choose 'desktop + EU East' as the configuration, and click the 'Start Test' button.
    Expectation: The speed test is executed. Following the advertisement display, the user is directed to the result page, where the selected device/region, target URL, and scores are displayed.
    """

    print('002 desktop test')
    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys(TARGET_URL)
    device_dropdown = driver.find_element(By.XPATH, DEVICE_DROPDOWN_XPATH)
    select = Select(device_dropdown)
    select.select_by_index(1)

    driver.find_element(By.XPATH, START_BTN_XPATH).click()
    print('waiting for the result...')

    testing_label = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, TESTING_LABEL_XPATH)))
    assert testing_label.text == 'Testing ' + TARGET_URL

    skip_link = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, SKIP_LINK_XPATH)))
    skip_link.click()

    assert driver.find_element(By.XPATH, URL_TEXT_XPATH).text == TARGET_URL.replace('https://', '')
    assert driver.find_element(By.XPATH, REGION_TEXT_XPATH).text == 'US EAST'
    assert driver.find_element(By.XPATH, DEVICE_TEXT_XPATH).text == 'DESKTOP FAST'
    assert len(driver.find_elements(By.CLASS_NAME, SCORE_CLASS)) == 2
    for score_element in driver.find_elements(By.CLASS_NAME, SCORE_CLASS):
        assert re.match(r'\d{2}\%', score_element.text)


def test_empty_value(driver):
    """
    Test Scenario: Attempt to initiate a test by clicking the 'Start Test' button without entering a URL.
    Expectation: An error message briefly appears, and the user remains on the page without proceeding further.
    """

    print('003 empty value test')
    error_text = find_error_message(driver)
    assert error_text == 'Enter a website URL to start the performance test'
    assert driver.current_url == BASE_URL


def test_invalid_url(driver):
    """
    Test Scenario: Enter the invalid URL and click 'Start Test' button.
    Expectation: An error message briefly appears, and the user remains on the page without proceeding further.
    """

    print('004 invalid url test')
    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys('url')
    error_text = find_error_message(driver)
    assert error_text == 'URL must include \'.\'.'
    assert driver.current_url == BASE_URL


def test_non_exit_url(driver):
    """
    Test Scenario: Enter the URL that doesn't exist and click 'Start Test' button.
    Expectation: The speed test is executed. Following the advertisement display, the user is directed to the result page. The target URL is displayed, but the scores are marked as N/A.
    """

    print('005 invalid url test')
    non_exit_url = 'https://notexisting.co.jp'
    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys(non_exit_url)

    driver.find_element(By.XPATH, START_BTN_XPATH).click()
    print('waiting for the result...')

    testing_label = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, TESTING_LABEL_XPATH)))
    assert testing_label.text == 'Testing ' + non_exit_url

    skip_link = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, SKIP_LINK_XPATH)))
    skip_link.click()

    assert driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]').text == non_exit_url.replace('https://', '')
    assert len(driver.find_elements(By.CLASS_NAME, SCORE_CLASS)) == 2
    for score_element in driver.find_elements(By.CLASS_NAME, SCORE_CLASS):
        assert score_element.text == 'N/A'


def test_long_url(driver):
    """
    Test Scenario: Enter a long URL and click the 'Start Test' button.
    Expectation: An error message briefly appears for a second. The 'Start Test' button transitions to a loading status, but the user remains on the page without being redirected.
    """

    print('006 long url test')
    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys(LONG_URL)
    driver.find_element(By.XPATH, START_BTN_XPATH).click()

    assert driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/form/div/button/div').text == 'Loading...'
    assert driver.current_url == BASE_URL


def test_history(driver):
    """
    Test Scenario: Enter the URL to initiate a speed test, choose 'mobile + EU East' as the configuration, and click the 'Start Test' button. Then, return to the speed test page and click the 'Test History' link.
    Expectation: The previous test result is displayed on the history page.
    """

    print('007 history link test')
    test_mobile(driver)
    driver.get(BASE_URL)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/a[1]').click()

    h1_history = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/h1')))
    assert h1_history.text == 'Site Speed Test History'
    assert driver.current_url == 'https://www.debugbear.com/test/website-speed/history'

    assert driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/a').text == TARGET_URL


def test_sample_report(driver):
    """
    Test Scenario: Click 'View Sample Report' link.
    Expectation: The sample report page opens in a new tab.
    """

    print('008 sample report link test')
    initial_window_handle = driver.current_window_handle
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/a[2]').click()

    all_window_handles = driver.window_handles
    if len(all_window_handles) > 1:
        new_tab_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
        driver.switch_to.window(new_tab_handle)

    assert driver.current_url == 'https://www.debugbear.com/test/website-speed/ac4OZAut/overview'


def test_x_link(driver):
    """
    Scenario: Click 'Share Tool On Twitter' link.
    Expectation: The X website opens in a new tab.
    """

    print('009 x link test')
    initial_window_handle = driver.current_window_handle
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/a[3]').click()

    all_window_handles = driver.window_handles
    if len(all_window_handles) > 1:
        new_tab_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
        driver.switch_to.window(new_tab_handle)

    assert driver.current_url == 'https://twitter.com/DebugBear/status/1582302537302315008'


def test_report(driver):
    """
    Test Scenario: Enter the URL to initiate a speed test, choose 'desktop + EU East' as the configuration, and click the 'Start Test' button.
    Expectation: The speed test is executed. Following the advertisement display, the user is directed to the result page. The navigation links take users to each detailed report page. Each page displays specific metrics.
    """

    print('010 detailed report test')

    url_elem = driver.find_element(By.XPATH, URL_INPUT_XPATH)
    url_elem.send_keys(TARGET_URL)
    device_dropdown = driver.find_element(By.XPATH, DEVICE_DROPDOWN_XPATH)
    select = Select(device_dropdown)
    select.select_by_index(1)

    driver.find_element(By.XPATH, START_BTN_XPATH).click()
    print('waiting for the result...')

    testing_label = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, TESTING_LABEL_XPATH)))
    assert testing_label.text == 'Testing ' + TARGET_URL

    skip_link = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, SKIP_LINK_XPATH)))
    skip_link.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, URL_TEXT_XPATH)))
    for navi_elem in driver.find_elements(By.CLASS_NAME, 'page-load-nav__item-content'):
        navi_elem.click()
        driver.implicitly_wait(5)
        content_elm = driver.find_element(By.CLASS_NAME, 'pageload-tab')

        if navi_elem.text in ['Overview', 'Web Vitals', 'Requests', 'Lighthouse']:
            for metric in METRICS[navi_elem.text]:
                assert metric in content_elm.text


def find_error_message(driver):
    i = 0
    while i < RETRIES:
        try:
            driver.find_element(By.XPATH, START_BTN_XPATH).click()
            error_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'dbb-notification'))).text
            if error_text == '':
                raise TimeoutException()

            return error_text
        except TimeoutException:
            i = i + 1
            print("Cannot find the error message, Retrying... (%(i)s/%(max)s)" % {'i': i, 'max': RETRIES})
            continue
