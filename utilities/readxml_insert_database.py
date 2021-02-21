import xml.etree.ElementTree as ET
import mysql.connector as connector

tree = ET.parse("E:\\NOP BO Automation\\test_data\\Discount.xml")
root = tree.getroot()

db_conn = connector.connect(host="localhost", user="root", passwd="Shonya@0803")
db_cursor = db_conn.cursor()
db_cursor.execute("use nop_admin")

for items in root.iter():
    if items.tag == "DiscountName":
        discount_name = items.text
    elif items.tag == "DiscountType":
        discount_type = items.text
    elif items.tag == "DiscountStartDate":
        discount_start_date = items.text
    elif items.tag == "DiscountEndDate":
        discount_end_date = items.text
    elif items.tag == "DiscountContect":
        discount_content = items.text

        db_query = "insert into discount (discount_name, discount_type, discount_start_date, discount_end_date, discount_admin_contect) " \
                   "values (%s, %s, %s, %s, %s)"
        db_cursor.execute(db_query, (discount_name, discount_type, discount_start_date, discount_end_date, discount_content))

db_conn.commit()
db_conn.close()
print("Items Inserted Successfully!")




