from selenium.webdriver import Chrome
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from test_case_1.test_scripts import scenario_1, scenario_2, scenario_3


def driver_finder():
    try:
        driver = Chrome()
    except selenium.common.exceptions.WebDriverException:
        driver = Chrome(ChromeDriverManager().install())
    finally:
        return driver


scenario_1(driver_finder())
scenario_2(driver_finder())
scenario_3(driver_finder())



