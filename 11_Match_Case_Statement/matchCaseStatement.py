# Calculator Example

number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))
operator = input("Enter the operator: +, -, *, /: ")

match operator:
    case '+':
        print(number_1 + number_2)
    case '-':
        print(number_1 - number_2)
    case '*':
        print(number_1 * number_2)
    case '/':
        print(number_1 / number_2)
    case _:
        print("Enter the correct operator")     