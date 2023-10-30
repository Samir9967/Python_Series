# d = {1:{'name':'samir','gf':'adu'},2:{'name':'adu'},3:{'name':'aditi'}}
# print(d)
# # print(d[1]['name'])
# d[1]['name']='aditi ghadi'
# print(d)

                                    # iterating nested dictionary
# d = {
#     101:{'name':'samir','age':24},
#     102:{'name':'aditi','age':20},
#     103:{'name':'panda','age':20}
# }

# for i,j in d.items():
#     print(f'id is {i}')
#     for k in j:
#         print(f'{k} is : {j[k]}')

d = {'a':100,'b':200,'c':300}
a = 0
for i in d:
    s = d[i]
    a = a + s
print(a)
