start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))
total = 0
if (start_number > 0 and end_number > start_number):
    while (start_number <= end_number):
        total = total + start_number
        start_number = start_number + 1

print(total)