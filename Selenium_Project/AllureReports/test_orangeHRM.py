import allure
from allure_commons.model2 import Attachment
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

#Уточняем куда pytest сохранит файлы Allure
# pytest -v -s --alluredir="C:\Users\Timelord\PycharmProjects\Selenium_Project\AllureReports" .\test_orangeHRM.py

#Из bat Allure генерируем отчет находясь прямо в его директории
#.\allure serve C:\Users\Timelord\PycharmProjects\Selenium_Project\AllureReports

@allure.severity(allure.severity_level.NORMAL)  # severity level can be applied to class or method
class TestOrangeHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[1]/img").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

        # this test will be skipped

    def test_list_employees(self):
        pytest.skip("Skipping this test")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        self.driver.find_element(By.XPATH,
                                 "// *[ @ id = 'app'] / div[1] / div / div[1] / div / div[2] / div[2] / form / div[3] / button").click()

        # verification
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":  # this is done intentionally to fail the Test
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), "testLoginSreen",
                          attachment_type=Attachment.type.PNG)  # this generates and saves Allure report on the Test Fail step
            self.driver.close()
            assert False

