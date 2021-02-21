import xml.etree.ElementTree as ET
import mysql.connector

tree = ET.parse("Test_Cust.xml")
root = tree.getroot()
l = len(root)

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Shonya@0803")
mycursor = myconn.cursor()
mycursor.execute("use nop_admin")

for length in range(0,l):
    for items in root[length]:
        if items.tag == "Email":
            user_email = items.text
        elif items.tag == "CompanyName":
            cust_company = items.text
        elif items.tag == "FirstName":
            first_name = items.text
        elif items.tag == "LastName":
            last_name = items.text

            sql_query = "insert into customers (cust_email,cust_firstname,cust_lastname,cust_companyname) values (%s,%s,%s,%s)"
            mycursor.execute(sql_query, (user_email,first_name,last_name,cust_company))
            myconn.commit()


print("Records Inserted")

