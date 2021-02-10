from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()

class Home_Page:
    catalog_link_xpath = "//span[text()='Catalog']"
    catalogproducts_link_xpath = "//span[text()='Products']"

    def __init__(self, driver):
        self.driver = driver

    def test_click_catalog_products_link (self):
        self.driver.find_element_by_xpath(self.catalog_link_xpath).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH , self.catalogproducts_link_xpath)))
        self.driver.find_element_by_xpath(self.catalogproducts_link_xpath).click()