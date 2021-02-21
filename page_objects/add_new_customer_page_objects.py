from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Add_New_Customer:
    email_field_xpath = "//input[@id='Email']"
    firstname_field_xpath = "//input[@id='FirstName']"
    lastname_field_xpath = "//input[@id='LastName']"
    company_field_xpath = "//input[@id='Company']"
    save_button_xpath = "//button[@name='save']"
    add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_add_new_customer(self, email, first_name, last_name, company):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath)))
        self.driver.find_element_by_xpath(self.email_field_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.firstname_field_xpath).send_keys(first_name)
        self.driver.find_element_by_xpath(self.lastname_field_xpath).send_keys(last_name)
        self.driver.find_element_by_xpath(self.company_field_xpath).send_keys(company)
        self.driver.find_element_by_xpath(self.save_button_xpath).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, self.add_button_xpath)))
        self.driver.find_element_by_xpath(self.add_button_xpath).click()