import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = 'store',default = 'chrome'
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome("E:\\chromedriver-win64\\chromedriver")
    elif browser_name == "edge":
        driver = webdriver.Edge("E:\\edgedriver_win64\\msedgedriver")

    driver.get("https://www.expressoqa.com/Logon.aspx")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "ctl00_cphMain_Login1_UserName").send_keys("skaluvala")
    driver.find_element(By.ID, "ctl00_cphMain_Login1_Password").send_keys("Expresso#123")
    driver.find_element(By.CSS_SELECTOR, "#ctl00_cphMain_Login1_LoginButton").click()
    request.cls.driver = driver

    # yield
    # driver.close()









