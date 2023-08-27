# Bytes
number = [10,20,30,40,255]        #list
num = bytes(number)

for i in num:
    print(i)                     # accessing all element by loop

print(type(num))


# number2 = [12,456,89,34]                # error bytes must be in range between 0 to 255
# num2 = bytes(number2)
# for i in num2:
#     print(i)

# number2 = [-12,46,89,34]                # error bytes can not hold negative number
# num2 = bytes(number2)
# for i in num2:
#     print(i)

number2 = [12,46,89,34]                # error bytes must be in range between 0 to 255
# number2[2]=90
num2 = bytes(number2)
# num2[2] = 90                          # error can not modify the element
for i in num2:
    if i == 1:
        i[0] = 23
    print(i)