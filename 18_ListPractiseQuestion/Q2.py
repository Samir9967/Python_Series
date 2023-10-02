# write a program to check whether lucky number is present in list or not until its find
num = [1,2,4,6,8,10,23,34,45,56,78,90]
choice = int(input("Enter the number: "))

while True:
    if choice in num:
        print("yes")
        break
    else:
        print("Noooo")
        choice = int(input("Enter the number again: "))