import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Add_Product:

    productname_feild_xpath = "//input[@id='Name']"
    descriptionframe_frame_id = "FullDescription_ifr"
    description_field_xpath = "//body[@id='tinymce']"
    sku_field_xpath = "//input[@id='Sku']"
    dropdown_categories_xpath = "//select[@id='SelectedCategoryIds']"
    dropdown_manufacturers_xpath = "//select[@id='SelectedManufacturerIds']"
    saveandcontinue_button_xpath = "//button[@name='save-continue']"
    uploadfile_button_xpath = "(//input[@title='file input'])[1]"
    save_button_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def test_add_new_product(self,productname,description,sku,uploadimgpath):
        wait = WebDriverWait (self.driver, 30)

        self.driver.find_element_by_xpath(self.productname_feild_xpath).send_keys(productname)
        self.driver.switch_to_frame(self.descriptionframe_frame_id)
        self.driver.find_element_by_xpath(self.description_field_xpath).send_keys(description)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath(self.sku_field_xpath).send_keys(sku)
        time.sleep(4)
        self.driver.find_element_by_xpath(self.saveandcontinue_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.uploadfile_button_xpath).send_keys(uploadimgpath)
        print("Image Uploaded successfully")
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        time.sleep(4)
        self.driver.switch_to_alert().accept()


