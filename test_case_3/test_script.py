import time

def scenario_test(driver):
    letters = ["m", "l", "q", "z"]
    driver.get("http://the-internet.herokuapp.com/key_presses")
    target = driver.find_element_by_id("target")
    for i in letters:
        target.send_keys(i)
        result = driver.find_element_by_id("result")
        assert result.text == f"You entered: {i.upper()}"
        time.sleep(3)
    driver.close()