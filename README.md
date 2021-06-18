# searchability_selenium_test

Tests for Searchability assessment.

Using http://the-internet.herokuapp.com/

###### Dependencies:
Built with Python3.9 using Selenium to execute automation.

To install Python extensions, CD into root directory and run:

`pip install - r requirements.txt
`
###### Test case 1:
Using the form authentication sample.

Testing the authentication form to see how it behaves with the following scenarios:

Scenario 1: User enters correct username and incorrect password.

Scenario 2: User enters incorrect username and correct password.

Scenario 3: User enters correct username and correct password and logs out.

Run tests by running /test_case_1/answer_digital_auto_test.py


###### Test case 2:
Using Infinite scroll sample.

Testing to see how infinite scroll works on the webpage.

User scrolls to the bottom of the page twice, and then back to the top and then confirms "Infinite scroll" is on the webpage.

Run tests by running /test_case_2/infinite_scroll.py

###### Test case 3:
Using Key presses example.

Testing behaviour of webpage when keys are pressed.

User presses 4 keys and checks webpage response after each key press, respectively.

Run tests by running /test_case_3/ke_presses.py
