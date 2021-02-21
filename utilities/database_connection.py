from mysql import connector

class DB_Validation:

    items_from_db  = ()
    item_from_db = ""

    @staticmethod
    def db_validation_product_check(hostname, db_user, db_password, db_name, sql_query):
        myconnection = connector.connect(host=hostname, user=db_user, passwd=db_password)
        mycursor = myconnection.cursor()
        mycursor.execute(db_name)
        mycursor.execute(sql_query)

        for items in mycursor:
            db_product_name = items[0]
            DB_Validation.item_from_db = db_product_name

        myconnection.commit()
        mycursor.close()

    @staticmethod
    def db_validation_return_all_records(hostname, db_user, db_password, db_name, sql_query):
        myconnection = connector.connect(host=hostname, user=db_user, passwd=db_password)
        mycursor = myconnection.cursor()
        mycursor.execute(db_name)
        mycursor.execute(sql_query)

        res = mycursor.fetchall()
        print(res)
        DB_Validation.items_from_db = res

        myconnection.commit()
        mycursor.close()

    @staticmethod
    def db_validation_update_query(hostname, db_user, db_password, db_name, sql_query):
        myconnection = connector.connect(host=hostname, user=db_user, passwd=db_password)
        mycursor = myconnection.cursor()
        mycursor.execute(db_name)
        mycursor.execute(sql_query)

        myconnection.commit()
        mycursor.close()