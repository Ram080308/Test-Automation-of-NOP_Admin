from selenium import webdriver


class Create_Campaigns:
    add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_click_add_campaign(self):
        self.driver.find_element_by_xpath(self.add_button_xpath).click()