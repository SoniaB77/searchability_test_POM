

def scenario_1(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("tomsmith")
    password.send_keys("jeffgoldblum")
    login = driver.find_element_by_class_name("fa-sign-in")
    login.click()
    flash_message = driver.find_element_by_id("flash").text
    assert flash_message.startswith("Your password is invalid!")
    driver.close()


def scenario_2(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("CaptainMarvel")
    password.send_keys("SuperSecretPassword!")
    login = driver.find_element_by_class_name("fa-sign-in")
    login.click()
    flash_message = driver.find_element_by_id("flash").text
    assert flash_message.startswith("Your username is invalid!")
    driver.close()


def scenario_3(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login = driver.find_element_by_class_name("fa-sign-in")
    login.click()
    flash_message = driver.find_element_by_id("flash").text
    assert flash_message.startswith("You logged into a secure area!")
    logout = driver.find_element_by_class_name("icon-signout")
    logout.click()
    flash_message = driver.find_element_by_id("flash").text
    assert flash_message.startswith("You logged out of the secure area!")
    driver.close()
