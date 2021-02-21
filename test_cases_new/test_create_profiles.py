from dummy_code.xml_to_excelsheet import Xml_to_ExcelSheet
from page_objects.add_new_customer_page_objects import Add_New_Customer
from page_objects.customers_landing_page_objects import Customers_LandingPage
from page_objects.home_page_objects import Home_Page
from page_objects.login_page_objects import Login_Page
from utilities.read_config import Read_config
from utilities import read_excel_data
from selenium import webdriver
#driver = webdriver.Chrome()

class Test_Create_Customer_Profiles:


    Xml_to_ExcelSheet.xmldata_to_excel_sheet()

    url = Read_config.get_app_url()
    user_name = Read_config.get_user_name()
    user_password = Read_config.get_password()

    path = "E:\\NOP BO Automation\\test_data\\CustDetails.xlsx"
    sheet_name = "Sheet1"

    def test_create_customer_profiles(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.lp = Login_Page(self.driver)
        self.lp.test_login_to_application(self.user_name, self.user_password)

        self.hp = Home_Page(self.driver)
        self.hp.test_click_cusromers_link()

        self.clp = Customers_LandingPage(self.driver)
        self.clp.test_click_add_button()

        self.anc = Add_New_Customer(self.driver)

        rows = read_excel_data.get_row_count(self.path, self.sheet_name)
        print("My Rows = " , rows)
        for r in range(2,rows+1):
            mail = read_excel_data.read_data(self.path, self.sheet_name,r,1)
            fn = read_excel_data.read_data(self.path, self.sheet_name,r,2)
            ln = read_excel_data.read_data(self.path, self.sheet_name,r,3)
            company = read_excel_data.read_data(self.path, self.sheet_name,r,4)

            self.anc.test_add_new_customer(mail,fn,ln,company)

        self.driver.close()














