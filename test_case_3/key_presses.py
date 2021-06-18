from selenium.webdriver import Chrome
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from test_case_3.test_script import scenario_test


def driver_finder():
    try:
        driver = Chrome()
    except selenium.common.exceptions.WebDriverException:
        driver = Chrome(ChromeDriverManager().install())
    finally:
        return driver


scenario_test(driver_finder())