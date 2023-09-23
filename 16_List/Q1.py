# write a program to printing all the element from list along with positive and negative index

num = [12,13,123,54,67,134]

length = len(num)
for i in range(length):
    print(num[i], "Positive index: ", i, "negative index: ",i - length)