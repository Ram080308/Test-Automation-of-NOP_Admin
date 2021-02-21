import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome("E:\\NOP BO Automation\\browser_drivers\\chromedriver.exe")
    return driver

