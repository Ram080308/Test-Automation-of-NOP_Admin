from page_objects.home_page_objects import Home_Page
from utilities.read_config import Read_config
from page_objects.login_page_objects import Login_Page
from utilities.test_case_report_db import TestCase_Results


class Test_login_to_application:
    class_name = (__qualname__)
    test_case_id = "101"
    test_case_name = "Login to application"

    baseurl = Read_config.get_app_url()
    username = Read_config.get_user_name()
    password = Read_config.get_password()

    def test_login_to_portal(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.username, self.password)

        #query = "insert into sanity values ('"+self.test_case_id+"', '"+self.test_case_name+"', NOW(), 'PASS')"
        query = "update sanity set test_status = 'differed' where test_case_id = '"+self.test_case_id+"'"
        print(query)
        tcc = TestCase_Results()
        tcc.test_case_report_from_db(query)
        self.driver.close()







