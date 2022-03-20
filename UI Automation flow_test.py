import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_amazon():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_id("twotabsearchtextbox").send_keys("IPhone")
    time.sleep(1)
    driver.find_element_by_id("nav-search-submit-button").click()
    time.sleep(1)
    print(driver.find_element_by_xpath("//*[@id='search']/span/div/h1/div/div[1]/div/div/span[1]").text)
    time.sleep(1)
    driver.close()
