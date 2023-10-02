# write a program to print a list in reverse order

num = [10,20,30,40,50]
# n = len(num)-1
n = -1

# for i in range(4,-1,-1):
#     print(num[i])

# while n >= 0:
#     print(num[n])
#     n = n - 1

while n >= -len(num):
    print(num[n])
    n = n - 1