
class Login_Page:

    email_feild_xpath = "//input[@id='Email']"
    password_field_xpath = "//input[@id='Password']"
    submit_button_xpath = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def test_login_to_application(self, username, password):

        self.driver.find_element_by_xpath(self.email_feild_xpath).clear()
        self.driver.find_element_by_xpath(self.email_feild_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.password_field_xpath).clear()
        self.driver.find_element_by_xpath(self.password_field_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()
