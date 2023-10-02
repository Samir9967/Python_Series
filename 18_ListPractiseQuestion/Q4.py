# write a program to find out min and max in given list
num = [10,3,2,1,70,12]
min_num = num[0]
max_num = num[0]

for i in num:
    if i < min_num:
        min_num = i
print(min_num)

for i in num:
    if i > max_num:
        max_num = i
print(max_num)