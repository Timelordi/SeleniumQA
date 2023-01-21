import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Windows.html")
#driver.maximize_window()

#Определяем все элементы на которые будем наводить мышью
Switch_to = driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
alerts = driver.find_element(By.XPATH,"//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[1]/a")

#решено двойным кликом просто выделять кусочек текста
text_field = driver.find_element(By.XPATH, "//*[@id='Tabbed']/p")
#прикрепляем к ActionChain наш драйвер
actions = ActionChains(driver)
#выполняем двойнок клик на элементе который нашли
actions.double_click(text_field).perform()
time.sleep(3)

#находим кнопку со значком фейсбук
facebook_button = driver.find_element(By.XPATH, "//*[@id='footer']/div/div/div[2]/a[1]/span")
actions.context_click(facebook_button).perform()  #нажимаем на кнопку со значком фейсбук
time.sleep(5)
actions.click(driver.find_element(By.XPATH, "/html/body/div[1]/div")).perform() #щелкаем в пустом месте

#наводим на выпадающий элемент и в конце кликаем на дочерний
actions.move_to_element(Switch_to).move_to_element(alerts).click().perform()