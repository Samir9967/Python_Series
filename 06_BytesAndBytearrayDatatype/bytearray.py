number = [10,20,30,40]
num = bytearray(number)
for i in num:
    print(i)

# number2 = [10,234,555,667]    #error

# can be modify in bytearray
num[2]=200
for i in num:
    print(i)