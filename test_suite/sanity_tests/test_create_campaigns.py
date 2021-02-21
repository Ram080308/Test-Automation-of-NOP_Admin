import time

from page_objects.add_new_campaign_page_objects import Add_New_Campaign
from page_objects.campaigns_landing_page_objects import Create_Campaigns
from page_objects.home_page_objects import Home_Page
from page_objects.login_page_objects import Login_Page
from utilities.database_connection import DB_Validation
from utilities.read_config import Read_config


class Test_Create_Campaigns:
    baseurl = Read_config.get_app_url()
    username = Read_config.get_user_name()
    password = Read_config.get_password()

    db_host = Read_config.get_db_host()
    db_username = Read_config.get_db_username()
    db_password = Read_config.get_db_password()
    db_dbname = Read_config.get_db_name()


    def test_login_to_portal(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.username, self.password)

        self.hp = Home_Page(self.driver)
        self.hp.test_click_campaign_link()

        self.cm = Create_Campaigns(self.driver)
        self.cm.test_click_add_campaign()
        time.sleep(4)
        sql_query = "select * from campaign"
        DB_Validation.db_validation_return_all_records(self.db_host, self.db_username, self.db_password, self.db_dbname, sql_query)
        my_items = DB_Validation.items_from_db

        self.addnew = Add_New_Campaign(self.driver)
        for elements in my_items:
            campaign_name = elements[0]
            body_message = elements[1]
            date = elements[3]
            email = elements[2]
            self.addnew.test_create_campaign(campaign_name,body_message,date,email)

        print("Items processed successfully!")
        self.driver.close()








