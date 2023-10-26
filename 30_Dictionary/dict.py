# myinfo = {'name':'samir','age':24,'gf':'adu'}
# print(myinfo,type(myinfo))
# print(myinfo['gf']) 


                  # create empty dict and then add item
# myinfo = {}           # --> this is empty dict
# myinfo['name'] = 'adu'
# myinfo['age'] = 20
# # print(myinfo)

                          # to check specified key is exist or not
# name = {1:'sam',2:'adu',3:"true"}
# print(2 in name)

                              # create a dict by taking user input
# d = {}

# while True:
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     d[key] = value

#     choice = input('Do u need again to input key and value: [y/n]')
#     if(choice == 'n'):
#         break

# print(d)

# for i in range(1,4):
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     d[key] = value

# print(d)

                         # traversing the list
myinfo = {'name':'samir','age':24,'gf':'adu'}
# for i in myinfo:
#     print(i, myinfo[i])

                            # add items in dictionary
# print(myinfo)
myinfo['gf2'] = 'panda'
print(myinfo)

                          # delete item
# del myinfo['name']
# print(myinfo)

                            # delete all items
# myinfo.clear()
# print(myinfo)

                              # delete dict
del myinfo
print(myinfo)