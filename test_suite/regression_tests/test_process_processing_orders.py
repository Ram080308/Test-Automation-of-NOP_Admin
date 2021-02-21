from page_objects.edit_orders_page_objects import Edit_Orders
from page_objects.home_page_objects import Home_Page
from page_objects.login_page_objects import Login_Page
from page_objects.orders_landing_page_objects import Orders_LandingPage
from utilities.read_config import Read_config


class Test_Process_ProcessingOrders:
    baseurl = Read_config.get_app_url()
    username = Read_config.get_user_name()
    password = Read_config.get_password()

    def test_login_to_portal(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.username, self.password)

        self.hp = Home_Page(self.driver)
        self.hp.test_click_more_info_orders()

        self.olp = Orders_LandingPage(self.driver)
        self.olp.test_process_the_orders("Processing")

        self.eo = Edit_Orders(self.driver)
        self.eo.test_order_status()

        self.driver.close()
