import datetime
import math
import json
import re
import os

list = [1, 3, 4, 4, 4, 8, "String"]
tuple = (1, 2, 4, 4, 4, 25, 12)
set = {11, 41, 54, 7, 2, 4, 4, 4}
dictionary = {1: "One", 2: "Two", 3: "Three", 8: "Eight", 10: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]}

# Проверить тип объекта
type(list)


# Lambda function
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(itemno, quantity, price))


# read from file
# f = open(r"C:\Users\Timelord\Downloads\test.txt")
# string = f.read()
# print(string)
# f.close()

# write to file
# f = open(r"C:\Users\Timelord\Downloads\test.txt", "w") # если использовать "a" то текст будет дополняться
# write_text = "This is a capital of Ukraine"
# f.write(write_text)
# f.close()

# remove file
# os.remove(r"C:\Users\Timelord\Downloads\test.txt") #удаление файла

