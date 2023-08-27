Name = "Samir Maharana"

print(Name[1:15:1])
print("---------------->")
print(Name[15:0:-1])
print("_____________--------->")
print(Name[100:12:2])      #empty
print("___________________________>")
print(Name[::-1])
print("____________________________>")
print(Name[-15:-14:-1])     #empty
print("______________________________>")
print(Name[8:15:-1])         #empty
print(Name[5000:2:-1])

message = "Welcome to python"
# print(message[-6::])
# print(message[-1:-4:-1])
# print(message[:-4:])
# print(message[-4:-1:])
# print(message[-4:-17:-1])
# print(message[2:9])
# print(message[2:])
# print(message[::-+1])

print(message[1:-12:])
print(message[-2:-12:])   #empty
print(message[True:-1:1])
print(message[False+10:(True-True):-1])