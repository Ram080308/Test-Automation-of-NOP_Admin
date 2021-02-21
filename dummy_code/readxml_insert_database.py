import xml.etree.ElementTree as ET
import mysql.connector

tree = ET.parse('/test_data/Discount.xml')
root = tree.getroot()
print(root)
all_cust = tree.findall("Discount")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Shonya@0803")
mycursor = myconn.cursor()
mycursor.execute("use nop_admin")

for discounts in all_cust:
    discount_name = discounts.find("DiscountName").text
    discount_type = discounts.find("DiscountType").text
    discount_start_date = discounts.find("DiscountStartDate").text
    discount_end_date = discounts.find("DiscountEndDate").text
    discount_admin_contect = discounts.find("DiscountContect").text

    sql_query = "insert into discount (discount_name, discount_type, discount_start_date, discount_end_date, discount_admin_contect) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql_query,(discount_name, discount_type, discount_start_date, discount_end_date, discount_admin_contect))
    myconn.commit()

print("Query Executed Successfully")
myconn.close()











