import xml.etree.ElementTree as ET
import mysql.connector as connector

tree = ET.parse("Test_Cust.xml")
root = tree.getroot()

db_con = connector.connect(host="localhost", user="root", passwd="Shonya@0803")
db_cursor = db_con.cursor()
db_cursor.execute("use nop_admin")

for items in root.iter():
    if items.tag == "Email":
        cust_email = items.text
    elif items.tag == "CompanyName":
        cust_cn = items.text
    elif items.tag == "FirstName":
        cust_fn = items.text
    elif items.tag == "LastName":
        cust_ln = items.text

        sql_query = "insert into customers (cust_email,cust_firstname,cust_lastname,cust_companyname) values (%s,%s,%s,%s)"
        db_cursor.execute(sql_query, (cust_email, cust_fn, cust_ln, cust_cn))

db_con.commit()
db_con.close()
print("Successfully Executed!")



