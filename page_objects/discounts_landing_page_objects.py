from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Discounts_Landing_Page:
    add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_click_add_button(self):
        wait = WebDriverWait(self.driver , 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.add_button_xpath)))
        self.driver.find_element_by_xpath(self.add_button_xpath).click()