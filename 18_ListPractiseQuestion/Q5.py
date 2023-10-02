#write a program to search a value from a list then display itts index 
# if the value is present multiple times then print its all index 
# and also count the number of times that value is repeated in the list

num = [10,20,30,20,40,50,10,20,50]
i = 0
count = 0
key = int(input("Enter the key: "))

while i < len(num):
    if key == num[i]:
        print(f'{key} is present at {i} index')
        count = count + 1
    i = i + 1
print(f'{key} total count is {count}')