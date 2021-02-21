from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()

class Add_New_Discount:
    name_field_xpath = "//input[@id='Name']"
    select_discount_type_dropdown_xpath = "//select[@id='DiscountTypeId']"
    startdate_date_xpath = "//input[@id='StartDateUtc']"
    enddate_date_xpath = "//input[@id='EndDateUtc']"
    admincontent_textarea_xpath = "//textarea[@id='AdminComment']"
    save_button_xpath = "//button[@name='save']"
    add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_add_discount(self, discount_name, discount_type, discount_sd, discount_ed, discount_adminarea):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath)))
        self.driver.find_element_by_xpath(self.name_field_xpath).send_keys(discount_name)
        dis_type = self.driver.find_element_by_xpath(self.select_discount_type_dropdown_xpath)
        value = Select(dis_type)
        value.select_by_visible_text(discount_type)
        self.driver.find_element_by_xpath(self.startdate_date_xpath).send_keys(discount_sd)
        self.driver.find_element_by_xpath(self.enddate_date_xpath).send_keys(discount_ed)
        self.driver.find_element_by_xpath(self.admincontent_textarea_xpath).send_keys(discount_adminarea)
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.add_button_xpath)))
        self.driver.find_element_by_xpath(self.add_button_xpath).click()
