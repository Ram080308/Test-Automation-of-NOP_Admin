

class GiftCard_Page:
    addnew_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def test_click_add_new_button(self):
        self.driver.find_element_by_xpath(self.addnew_button_xpath).click()
