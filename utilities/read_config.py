import configparser
config = configparser.RawConfigParser()
config.read("E:\\NOP BO Automation\\configuration\\config.ini")

class Read_config:
    @staticmethod
    def get_app_url():
        url = config.get("Login info" , "baseurl")
        print(url)
        return url

    @staticmethod
    def get_user_name():
        user_name = config.get("Login info" , "username")
        return user_name

    @staticmethod
    def get_password():
        password = config.get("Login info" , "password")
        return password

    @staticmethod
    def get_db_host():
        hostname = config.get("Database info" , "db_host_name")
        return hostname

    @staticmethod
    def get_db_username():
        db_username = config.get("Database info", "db_user_name")
        return db_username

    @staticmethod
    def get_db_password():
        db_passwrd = config.get("Database info", "db_password")
        return db_passwrd

    @staticmethod
    def get_db_name():
        db_name = config.get("Database info", "dn_name")
        return db_name

    @staticmethod
    def get_prd_query():
        prd_query = config.get("SQL Queries", "verify_product")
        return prd_query














