import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://www.sportsdirect.com/registration")
#Ждем пока загрузится
time.sleep(4)

#Соглашаемся с Куки
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

#Закрываем страничку выбора страны
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/button").click()
time.sleep(3)

#Заполняем текстовые поля
driver.find_element(By.ID, 'Registration_FirstName').send_keys("Bups")
driver.find_element(By.ID, 'Registration_LastName').send_keys("Polosatovich")
driver.find_element(By.ID, 'Registration_EmailAddress').send_keys("bupsopups@mail.ru")

#Делаем выбор в Drop down меню
#select by visible text
day_select = Select(driver.find_element(By.ID, 'Registration_DateOfBirthDay'))
day_select.select_by_visible_text('19')
#select by index
month_select = Select(driver.find_element(By.ID, 'Registration_DateOfBirthMonth'))
month_select.select_by_index(6)
#select by value
year_select = Select(driver.find_element(By.ID, 'Registration_DateOfBirthYear'))
year_select.select_by_value('1990')

#Посчитать количество элементов в Drop Down Menu
#print(len(day_select.options))
#print(len(month_select.options))
#print(len(year_select.options))

#Вывести содержимое Drop down менюшек
all_day_options = day_select.options
print("Days:")
for option in all_day_options:
    print(option.text)

all_month_options = month_select.options
print("Months:")
for option in all_month_options:
    print(option.text)

all_years_options = year_select.options
print("Years:")
for option in all_years_options:
        print(option.text)

#Заполняем пароль и повторно пароль
password = driver.find_element(By.ID, 'txtPassword').send_keys("Qwerty12")
password = driver.find_element(By.ID, 'Registration_ConfirmPassword').send_keys("Qwerty12")

#Работаем с Radio button
driver.find_element(By.XPATH, '//*[@id="Registration_IsSubscriber"]').click()

#ищем линки
links = driver.find_elements(By.TAG_NAME, "a")
print("Links", len(links))

#Нажимаем на Линк
driver.find_element(By.LINK_TEXT,"Terms & Conditions").click()
driver.back()

#нажимаем кнопку Register
driver.find_element(By.ID, 'RegistrationSubmit').click()

time.sleep(10)
