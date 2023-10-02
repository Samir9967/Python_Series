#create a new list from 2 existing list in python 
# l=['hi','hello']
# s = ['samir','aditi','panda','debri']
# output  = ['hi samir','hi aditi','hi panda','hi debri','hello samir','hello aditi','hello panda','hello debri']

greet = ['hi','hello']
name = ['samir','aditi','panda','debri']
fullname = []

for i in greet:
    for j in name:
        k = i + " " + j 
        fullname.append(k)
print(fullname)