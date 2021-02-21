
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.database_connection import DB_Validation



class Add_New_Campaign:
    name_field_xpath = "//input[@id='Name']"
    subject_field_xpath = "//input[@id='Subject']"
    body_textarea_xpath = "//textarea[@id='Body']"
    date_picker_xpath = "//input[@data-role='datetimepicker']"
    saveandcontinue_button_xpath = "//button[@name='save-continue']"
    email_field_xpath = "//input[@id='TestEmail']"
    button_save_xpath = "//button[@name='save']"
    add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_create_campaign(self, camp_name, body_message, date, user_email):

        self.driver.find_element_by_xpath(self.name_field_xpath).send_keys(camp_name)
        self.driver.find_element_by_xpath(self.subject_field_xpath).send_keys("Hello Campaign details")
        self.driver.find_element_by_xpath(self.body_textarea_xpath).send_keys(body_message)
        self.driver.find_element_by_xpath(self.date_picker_xpath).send_keys(date)
        self.driver.find_element_by_xpath(self.saveandcontinue_button_xpath).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.email_field_xpath)))
        self.driver.find_element_by_xpath(self.email_field_xpath).send_keys(user_email)
        self.driver.find_element_by_xpath(self.button_save_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.add_button_xpath)))
        self.driver.find_element_by_xpath(self.add_button_xpath).click()




