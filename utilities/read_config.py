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





