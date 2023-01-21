from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

#кастомизируем путь сохранения файла
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "D:/"})

#добавляем кастомизированный путь в инициализацию драйвера
driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe", chrome_options=chromeOptions)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download text file
driver.find_element(By.ID, "textbox").send_keys("Testing by Dmitriy")
driver.find_element(By.ID, "createTxt").click() #generate file button
time.sleep(1)
driver.find_element(By.ID, "link-to-download").click() #download link



