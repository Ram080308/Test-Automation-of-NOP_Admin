import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Create_Giftcard:

    giftcardtype_dropdown_xpath = "//select[@id='GiftCardTypeId']"
    activated_checkbox_xpath = "//input[@class='check-box']"
    generatecode_button_xpath = "//button[@id='generateCouponCode']"
    cuponcode_field_xpath = "//input[@id='GiftCardCouponCode']"
    recepiantname_field_xpath = "//input[@id='RecipientName']"
    save_button_xpath = "//button[@name='save']"

    global_my_gift_card = ""

    def __init__(self,driver):
        self.driver = driver


    def test_create_new_giftcard(self, gc_type, gc_rec_name):
        wait = WebDriverWait(self.driver, 30)
        gctype = self.driver.find_element_by_xpath(self.giftcardtype_dropdown_xpath)
        sel = Select(gctype)
        sel.select_by_visible_text(gc_type)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.activated_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.generatecode_button_xpath).click()
        time.sleep(3)
        my_gift_card = self.driver.find_element_by_xpath(self.cuponcode_field_xpath).get_attribute('value')
        self.driver.find_element_by_xpath(self.recepiantname_field_xpath).send_keys(gc_rec_name)
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        Create_Giftcard.global_my_gift_card = my_gift_card
        print(Create_Giftcard.global_my_gift_card, "Outside the method")


















