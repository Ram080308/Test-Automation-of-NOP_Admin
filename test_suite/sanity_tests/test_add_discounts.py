from page_objects.add_new_discounts_page_objects import Add_New_Discount
from page_objects.discounts_landing_page_objects import Discounts_Landing_Page
from page_objects.login_page_objects import Login_Page
from utilities.read_config import Read_config
from page_objects.home_page_objects import Home_Page
from utilities.database_connection import DB_Validation
from utilities import readxml_insert_database


class Test_Add_Discounts:
    url = Read_config.get_app_url()
    user_name = Read_config.get_user_name()
    user_password = Read_config.get_password()

    readxml_insert_database

    db_hostname = Read_config.get_db_host()
    db_username = Read_config.get_db_username()
    db_password = Read_config.get_db_password()
    db_name = Read_config.get_db_name()


    db_query = "select * from discount limit 3"
    DB_Validation.db_validation_return_all_records(db_hostname, db_username, db_password, db_name, db_query)
    all_items_from_db = DB_Validation.items_from_db
    length_of_items = len(all_items_from_db)

    def test_create_discounts(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.user_name, self.user_password)

        self.hp = Home_Page(self.driver)
        self.hp.test_click_discounts_link()

        self.dlp = Discounts_Landing_Page(self.driver)
        self.dlp.test_click_add_button()
        print("Clicked Add Button")

        self.alnewdis = Add_New_Discount(self.driver)
        for elements in self.all_items_from_db:
            discount_name = elements[0]
            discount_type = elements[1]
            discount_start_date = elements[2]
            discount_end_date = elements[3]
            discount_content = elements[4]
            self.alnewdis.test_add_discount(discount_name,discount_type,discount_start_date,discount_end_date,discount_content)

        self.driver.close()













