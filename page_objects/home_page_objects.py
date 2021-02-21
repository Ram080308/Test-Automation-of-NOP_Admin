import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_Page:
    catalog_link_xpath = "//span[text()='Catalog']"
    catalogproducts_link_xpath = "//span[text()='Products']"
    sales_link_xpath = "//span[text()='Sales']"
    salesgiftcards_link_xpath = "//span[text()='Gift cards']"
    promotions_link_xpath = "//span[text()='Promotions']"
    promotions_Campaigns_link_xpath = "//span[text()='Campaigns']"
    discounts_promotions_link_xpath = "//span[text()='Discounts']"
    ordersmoreinfo_link_xpath = "(//a[@class='small-box-footer'])[1]"
    customer_link_xpath = "(//span[text()='Customers'])[1]"
    customerinside_link_xpath = "(//span[text()='Customers'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def test_click_catalog_products_link (self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_xpath(self.catalog_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH , self.catalogproducts_link_xpath)))
        self.driver.find_element_by_xpath(self.catalogproducts_link_xpath).click()

    def test_click_sales_giftcards_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.sales_link_xpath)))
        self.driver.find_element_by_xpath(self.sales_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.salesgiftcards_link_xpath)))
        self.driver.find_element_by_xpath(self.salesgiftcards_link_xpath).click()

    def test_click_campaign_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.promotions_link_xpath)))
        self.driver.find_element_by_xpath(self.promotions_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.promotions_Campaigns_link_xpath)))
        self.driver.find_element_by_xpath(self.promotions_Campaigns_link_xpath).click()

    def test_click_more_info_orders(self):
        self.driver.find_element_by_xpath(self.ordersmoreinfo_link_xpath).click()

    def test_click_cusromers_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.customer_link_xpath)))
        self.driver.find_element_by_xpath(self.customer_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.customerinside_link_xpath)))
        self.driver.find_element_by_xpath(self.customerinside_link_xpath).click()

    def test_click_discounts_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.promotions_link_xpath)))
        self.driver.find_element_by_xpath(self.promotions_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.discounts_promotions_link_xpath)))
        self.driver.find_element_by_xpath(self.discounts_promotions_link_xpath).click()








   




