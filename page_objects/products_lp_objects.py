import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import database_connection


class Products_LandingPage:
    addnew_button_xpath = "//a[@class='btn bg-blue']"
    productname_field_xpath = "//input[@id='SearchProductName']"
    search_button_xpath = "//button[@id='search-products']"
    table_xpath = "//table[@id='products-grid']"


    def __init__(self,driver):
        self.driver = driver

    def test_click_addnew_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH , self.addnew_button_xpath)))
        self.driver.find_element_by_xpath(self.addnew_button_xpath).click()

    def test_verify_product_search_result(self, product_name, product_sku):
        self.driver.find_element_by_xpath(self.productname_field_xpath).send_keys(product_name)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

        time.sleep(5)
        table = self.driver.find_element_by_xpath(self.table_xpath)
        body = table.find_element_by_tag_name("tbody")
        rows = body.find_elements_by_tag_name("tr")
        row_count = len(rows)
        # product_from_db = database_connection.db_product_name

        for i in range(row_count):
            col = rows[i].find_elements_by_tag_name("td")
            for j in range(len(col)):
                if col[j].text == product_name:
                    break
        print("Item Present on site and inserted to DB successfully " , col[j].text)




