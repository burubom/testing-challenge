import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver

TIMEOUT = 120
RETRIES = 3
TARGET_URL = 'https://google.com'
BASE_URL = 'https://www.debugbear.com/test/website-speed'
URL_INPUT_XPATH = '//*[@id="app"]/div/div[1]/form/div/input'
START_BTN_XPATH = '//*[@id="app"]/div/div[1]/form/div/button'
DEVICE_DROPDOWN_XPATH = '//*[@id="app"]/div/div[1]/div[1]/select'
SKIP_LINK_XPATH = '/html/body/div[9]/div/div/div/div/div[2]/a[2]'
TESTING_LABEL_XPATH = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]'
URL_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]'
REGION_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/span'
DEVICE_TEXT_XPATH = '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[3]/span'
SCORE_CLASS = 'scale-3'


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
    url_elem.send_keys('http://www.reallylong.link/rll/7MectGPZ5J3v/1FXcH55HKNpbb0GDvW26Xto0TcYugBuWENSVtDF_2lkSfqWOgxYpehD9uFPB_YCFRFUzUaUCrZzd7AROmFNqeLsD4mlF3N6i4lIjVRKtD/vurZzGMbfA7qUFBHQgeKH3dUmqOhs/HY0db5fe0m8Gt96cM2LrYGz3itgzwv9yururtovnxOXAMUJoClRXAB4SSJ20ibnraxn4WEkweDMaecT5v6Huy_I4heleSuov9NeSCCt5HO00DFcCGwBfZBWR4/tAiOPKGmv02QS7l4wZk6sZ9vxXnpGGeY2Qs2HwOTOnIlfW2FR9dWnzZENVHs_HFYXTUxeVEeORlAyTW5ISRO/AFGrlb6fNWD0CQC3dX2zhPoI2oIxiwoO1ZIf6eknLqyJ1UXOrP/D0UI/Qd6EPDh3VkQwim15fpdBT2WOXkSmrtmalyoJ3PK3rU80Pqr0Qcjm/I6mM0h/wKQO2p1vQgcxgLZPrEYiNxkwdPXH9ZiSphsxKNrUJhzRH/H7QKXBs7pU20SUr1jPAQuHvJfIvluA5D_CwSd5z5mi6Y4LU7sJ3felqEcF/ZXeReoUH_ZBr6X2qopwThRweNxPhy/Kl8mqZm3_TKyJaxmHA/n3RuIxaVaogZCYMS6ZRgy6PptqYX1J5WVgj/7hpVENDwKg7e7IqA5NmuSVBtdXts2KObiwDszyTlM5mlTzlmbASrHcFXLbDBs0fsxp7MGXUCZHmgP4D/a4bxK7jurmZ/fn35t20aS3DOtO1ItVBfWcmgKLdgD3GOsbhZ2iiBqAnD7m/dQjZ8P4/jUMABpwIoXY7LOuj27__IrpqIyjTvEFOhqzu6nJv3ZKIx4WNja0s/7bSDz1XO9/oKq_1hpYeuk/wPn2nYtdEw/Rmc4tDP9oiC4S8yQh2yssa6PbJPy0EFu8Rw/81KpNW3OuQJeyYQGZbzX4UM1OBfJv10zOe4YTZE4mw50PAt9hIkZgWxYxdGccyQ29dDQhU6QKPIizxvUzc0bUBlcACMzxI1rNxhV4dZ1g9RtxlAunl6IYAVeLaIlip_r3K9fN8becW2wntFhc6MJT8ur9hAP/6kSrihA8gz_h0S8wSad4KY/zuUN4dF3U0uF4qKwuOz9adgQ0CjaOBPQi2EkjJMLZCsKLUsqCa52g9z4t5wU6s_cGyfuRMyA_WLY8pmimGevMxSVn2pj1pbQQH5TpleePNH_O876U4hxUsFMU8SM3ir3dvkiPlnuGepOPS8E2ONIMYT9WQc9yB_mNNx_wGh_gZWBbV1E1bVqn1CJC79X9zSued1NQabJva27RKZu8YqRVgLZiOLlBq1PI38k0gGsZLjIQCjWjE84n5jz8m_tsSmQyVvp1n8pzUp3aMlofGEqWH8X5rSwHaOsdU5_REDFEv3I6zPVaOV0UpnpK5iXPp4FMtItohXHqJeS7rq0rNEakqNBDtMrgKz9XTnoWBEU9oO4USoLof8CDk_0lL_HlnY6gX68EtbOAhTRQJHxHYIqC9o_R1IN0mpzhkHSN1yPLBklUC0RO_B/a0ng/pBTJtwRPhNjcdyQn8bfxtbQ/42KfE5TXNOEzJ/2mlmTlpNsASBYkacfoK6b3XAhMkHhEOSwtM2r_F4c15LBqr7wpDNSB3HDbuYB8/T6HJ_is2bwvrv1L6QDeZWlhTt7r_AF1kDt9qIR8TbanWxIvAnw0IIopt6u1VUqp7KahJCm7Kg4ZDDHElahdntZFyVg_BoAB67XM33jxu4SozpZqLMqf84kO5jOMQ5s2LOQWILInIXlt2LHxwds1qnHf9RdFxRUeU0GXU3zG5VxkuwpjMpkxC_G2d5yKHWmQCFlnnSg4b_POjBG6m4bk0WFLWhiKcxE_MI0_wPzL65_d2RLFbnI2Fanli/SHlW5ODpTgkfXnBkjpZ4PMJrN/3JmW9i87N4dW5Z8C1rj0w5bldtWBEBTrKSQSbIGxx')
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
