# Implicit typecasting

# num1 = 100
# num2 = 200.34
# total = num1 + num2
# print(total)
# print(type(total))

             # Explicit typecasting
              # other type to int()
#float to int
# num = int(12.34)
# print(num)

#complex to int
# num = int(12 + 12j)                  
# print(num)                #error

# bool to int
# num = int(True)
# print(num)

# num2 = int(True + True - False)
# print(num2)

 # String to int
# message = int("Hello Samir")
# print(message)                    #error

# String passing float to int
# message = int("12.34")
# print(message)                    #error

#String passing int value to int
# message = int("12")
# print(message)

                     #other type to float
#int to float
# num = float(12)
# print(num)

# complex to float     # error 

# bool to float
# num = float(True)
# print(num)

#String to float
# message = float("Hello")       # error

# message = float("12.45")
# print(message)

                                   # other to complex
# int and float to complex
# num = complex(12)
# print(num)

# bool to complex
# num = complex(True)
# print(num)

# String to complex
# message = complex("hello")             # error

# message = complex("12.45")
# print(message)

num = complex(12,10)
print(num)