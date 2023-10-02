# write a program to check wheather your lucky number is present inside list or not (user input)

num = [1,2,3,5,7,9,10,23,45,67,89,90]
choice = int(input("Enter the number: "))

if choice in num:
        print("yes")
else:
        print("No")