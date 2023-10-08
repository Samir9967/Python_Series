# num = [1,2,3,4,[5,6,7],8,9]
# print(num)
# print(num[4])
# print(num[4][1])

# num2 = [1,2,3,[4,5,6,[7,8,9]],10,11,12]
# print(num2[3])
# print(num2[3][1])
# print(num2[3][3])
# print(num2[3][3][2])

                           # nested as a matrix
num3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(num3[1])
# print(num3)

# for i in num3:
#     print(i)

# for i in num3:
#     for j in i:
#         print(j,end=' ')
#     print(" ")

num2 = [1,2,3,[4,5,6,[7,8,9]],10,11,12]
num2.reverse()
print(num2)