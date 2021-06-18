from selenium.webdriver.common.keys import Keys
import time


js_script = "window.scrollTo(0,document.body.scrollHeight)"

def scenario(driver):
    driver.get("http://the-internet.herokuapp.com/infinite_scroll")
    time.sleep(5)
    driver.execute_script(js_script)
    time.sleep(5)
    driver.execute_script(js_script)
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(3)
    assert "Infinite Scroll" in driver.page_source
    driver.close()
