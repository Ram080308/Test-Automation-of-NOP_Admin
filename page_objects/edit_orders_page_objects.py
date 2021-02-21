import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#driver = webdriver.Chrome()

class Edit_Orders:
    partialrefund_button_xpath = "//button[@id='partiallyrefundorderoffline']"
    arrows_up_xpath = "//span[@class='k-icon k-i-arrow-60-up']"
    refund_button_xpath = "//button[@id='partialrefundorder']"
    changestatus_button_xpath = "//button[@name='btnChangeOrderStatus']"
    status_selectdropdown_xpath = "//select[@id='OrderStatusId']"
    save_button_xpath = "//button[@id='btnSaveOrderStatus']"
    acknowledgeyes_button_xpath = "//button[@name='btnSaveOrderStatus']"

    def __init__(self,driver):
        self.driver = driver

    def test_order_status (self):
        wait = WebDriverWait(self.driver, 30)
        time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.partialrefund_button_xpath)))
        self.driver.find_element_by_xpath(self.partialrefund_button_xpath).click()

        main_page = self.driver.current_window_handle
        wh = self.driver.window_handles
        for allwh in wh:
            if allwh != main_page:
                next_page = allwh
                self.driver.switch_to_window(next_page)
                self.driver.maximize_window()
                wait.until(EC.element_to_be_clickable((By.XPATH, self.refund_button_xpath)))
                self.driver.find_element_by_xpath(self.arrows_up_xpath).click()
                self.driver.find_element_by_xpath(self.refund_button_xpath).click()

            self.driver.switch_to_window(main_page)
            time.sleep(3)
            self.driver.find_element_by_xpath(self.changestatus_button_xpath).click()
            order_status = self.driver.find_element_by_xpath(self.status_selectdropdown_xpath)
            self.os = Select (order_status)
            self.os.select_by_value("40")
            wait.until(EC.element_to_be_clickable((By.XPATH , self.save_button_xpath)))
            self.driver.find_element_by_xpath(self.save_button_xpath).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, self.acknowledgeyes_button_xpath)))
            self.driver.find_element_by_xpath(self.acknowledgeyes_button_xpath).click()






