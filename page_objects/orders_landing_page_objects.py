import time

from selenium import webdriver


class Orders_LandingPage:
    orders_table_xpath = "//table[@id='orders-grid']"
    view_link_xpath = "//a[@class='btn btn-default']"

    def __init__(self,driver):
        self.driver = driver

    def test_process_the_orders(self, status):
        time.sleep(3)
        table = self.driver.find_element_by_xpath(self.orders_table_xpath)
        body = table.find_element_by_tag_name("tbody")
        rows = body.find_elements_by_tag_name("tr")
        print(len(rows))
        all_view_links = self.driver.find_elements_by_xpath(self.view_link_xpath)
        print("Came to all viev links")

        try:
            for i in range(len(rows)):
                col = rows[i].find_elements_by_tag_name("td")
                for j in range(len(col)):
                    if col[j].text == status:
                        all_view_links[i].click()
                        break
        except:
            pass










