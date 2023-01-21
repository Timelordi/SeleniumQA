tuple = (3, 5, 6, True)

for i in tuple:
    print(i)
print("------")

el = 0
while el < tuple.__len__():
    print(tuple[el])
    el = el+1


