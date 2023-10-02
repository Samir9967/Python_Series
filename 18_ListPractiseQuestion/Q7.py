name = ["samir","aditi","panda"]
new_list = []

for i in name:
    n = len(i)
    new_list.append(i[0] + i[n-1])
print(new_list)