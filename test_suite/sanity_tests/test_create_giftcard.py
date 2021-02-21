from page_objects.add_new_giftcard_page_objects import Create_Giftcard
from page_objects.gift_card_page_objects import GiftCard_Page
from page_objects.home_page_objects import Home_Page
from page_objects.login_page_objects import Login_Page
from utilities import read_excel_data, database_connection
from utilities.database_connection import DB_Validation
from utilities.read_config import Read_config

class Test_Create_Giftcard:
    baseurl =  Read_config.get_app_url()
    username = Read_config.get_user_name()
    password = Read_config.get_password()

    path = "C:\\Users\\Ram\Desktop\\testdata.xlsx"
    sheet_name = "GiftCards"
    gctype = read_excel_data.read_data(path,sheet_name,2,1)
    my_gc_price = read_excel_data.read_data(path,sheet_name,2,2)
    strmygc = str(my_gc_price)
    gc_name = read_excel_data.read_data(path,sheet_name,2,3)

    db_host_name = Read_config.get_db_host()
    db_user_name = Read_config.get_db_username()
    db_password = Read_config.get_db_password()
    db_database_name = Read_config.get_db_name()

    def test_create_gift_card(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.username, self.password)

        self.hp = Home_Page(self.driver)
        self.hp.test_click_sales_giftcards_link()

        self.gcp = GiftCard_Page(self.driver)
        self.gcp.test_click_add_new_button()

        self.cgc = Create_Giftcard(self.driver)
        self.cgc.test_create_new_giftcard(self.gctype,self.gc_name)

        value_gc = Create_Giftcard.global_my_gift_card
        print(value_gc, "From Test Scenarios")
        update_query = "INSERT INTO gift_cards (cust_name,price,cupon_code) VALUES('Mike', '999' ,'"+value_gc+"')"
        self.bdv = DB_Validation()
        self.bdv.db_validation_update_query(self.db_host_name, self.db_user_name, self.db_password, self.db_database_name, update_query)
        print("Validated and Success !")

        self.driver.close()







