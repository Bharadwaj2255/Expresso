import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
from utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("CT_AddColumns_Data")
class Test_CustomTable(BaseClass):

    def test_CreateCT(self, CT_AddColumns_Data):
        self.driver.find_element(By.CSS_SELECTOR, "#select2-ctl00_drpChangeProgram-container").click()
        self.driver.find_element(By.XPATH, "//span/input[@type = 'search']").send_keys("Blue")
        # time.sleep(2)
        Programs = self.driver.find_elements(By.XPATH, "//span/ul/li[@class='select2-results__option']")
        print(len(Programs))
        list = []

        for Program in Programs:
            list.append(Program.text)
            if Program.text == "BlueMoon Vacation Ownership (4)":
                Program.click()
                break
        print(list)

        action = ActionChains(self.driver)

        action.move_to_element(self.driver.find_element(By.XPATH, "//li/a[text() = ' Content Management']")).perform()
        self.driver.find_element(By.ID, "ctl00_hyplnkCustomTables").click()

        frame1 = self.driver.find_element(By.ID, "ctl00_cphMain_iframeAngular")
        self.driver.switch_to.frame(frame1)

        left_grid = self.driver.find_element(By.XPATH, "//as-split-area[@class ='left-split-area as-split-area']")
        time.sleep(3)
        left_grid.find_element(By.XPATH, "//input[@type = 'search']").send_keys("2255")
        time.sleep(3)

        right_grid = self.driver.find_element(By.XPATH, "//as-split-area[@class = 'right-split-area as-split-area']")
        right_grid.find_element(By.XPATH, "(//input[@class = 'form-control form-control-sm ng-untouched ng-pristine ng-valid'])[1]").send_keys("Auto CT 2255")
        right_grid.find_element(By.CLASS_NAME, "ng-input").click()

        Primary_values = right_grid.find_elements(By.XPATH, "//div/div[@class = 'ng-option']")
        PV_list = []
        for Primary_value in Primary_values:
            PV_list.append(Primary_value.text)
            if Primary_value.text == "Split Name":
                Primary_value.click()
                break
        # print(PV_list)
        Add_columns = right_grid.find_element(By.XPATH, "(//button[text() = 'Add columns'])[2]")
        for i in range(3):
            Add_columns.click()
            time.sleep(1)

        right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[1]").send_keys(CT_AddColumns_Data[0])
        right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[2]").send_keys(CT_AddColumns_Data[1])
        right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[3]").send_keys(CT_AddColumns_Data[2])
        # right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[4]").send_keys(CT_AddColumns_Data[3])
        # right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[5]").send_keys(CT_AddColumns_Data[4])
        # right_grid.find_element(By.XPATH, "(//tbody/tr/div/div/input[@type = 'text'])[6]").send_keys(CT_AddColumns_Data[5])

        right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[2]").click()
        Col1 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        for col in Col1:
            if col.text == "Text":
                col.click()
                break

        right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[3]").click()
        Col2 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        for col2 in Col2:
            if col2.text == "Pdf":
                col2.click()
                break

        right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[4]").click()
        Col3 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        for col3 in Col3:
            if col3.text == "Image":
                col3.click()
                break

        # right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[5]").click()
        # Col4 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        # for col4 in Col4:
        #     if col4.text == "Image":
        #         col4.click()
        #         break
        #
        # right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[5]").click()
        # Col5 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        # for col5 in Col5:
        #     if col5.text == "PNG Image":
        #         col5.click()
        #         break
        #
        # right_grid.find_element(By.XPATH, "(//ng-select/div[@class='ng-select-container ng-has-value'])[6]").click()
        # Col6 = right_grid.find_elements(By.XPATH, "//div[@role = 'option']")
        # for col6 in Col6:
        #     if col6.text == "MMS Image":
        #         col6.click()
        #         break

        right_grid.find_element(By.XPATH, "//button[text()='Save']").click()
        Success = self.driver.find_element(By.XPATH, "//div/div/div/div[@role='alert']").text
        assert Success in "Saved successfully"
        print(Success)

        time.sleep(2)



    @pytest.fixture(params=[("ACT Name", "PDF", "Image")])
    def CT_AddColumns_Data(self, request):
        return request.param


    def test_create_tableRecord(self):
        self.driver.find_element(By.XPATH, "(//p/button[text() = 'New'])[2]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Primary Key']").send_keys("Test1")
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'ACT Name']").send_keys("ACT_test1")
        self.driver.find_element(By.XPATH, "//button[@title='Click to change the PDF']").click()
        self.driver.find_element(By.XPATH, "(//table/tbody/tr/td/button[@type = 'submit'])[5]").click()
        self.driver.find_element(By.XPATH, "//button[@title='Click to change the image']").click()
        self.driver.find_element(By.XPATH, "(//table/tbody/tr/td/button[@type = 'submit'])[5]").click()
        self.driver.find_element(By.XPATH, "//button[text() = 'Save']").click()
        save = self.driver.find_element(By.XPATH, "//div[@role = 'alert']").text
        assert "Saved success" in save
        print("git uploaded")
        print("git uploaded")
