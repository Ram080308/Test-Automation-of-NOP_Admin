from utilities.read_config import Read_config
from page_objects.login_page_objects import Login_Page


class Test_login_to_application:

    baseurl = Read_config.get_app_url()
    username = Read_config.get_user_name()
    password = Read_config.get_password()

    def test_login(self, setup):
        self.driver =setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.username, self.password)
        self.driver.close()



