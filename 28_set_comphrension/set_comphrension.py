                                 # using set from list
l = [1,2,3,4,5]
# s = set()

# for i in l:
#     s.add(i)

# print(s)

                                # set comphrension
                                # using set from list
# s = {i for i in l}
# print(s)

                                 # using range()
# s = {i for i in range(0,11)}
# print(s)

s = {i for i in range(20,41) if i%4==0}
print(s)

                   # create a list by adding first element of each list into set
names = ['samir','weds','aditi','panda']
# s = set()
# for i in names:
#     a = i[0]
#     s.add(a)
# print(s)

# s = {i[0] for i in names}
# print(s)

# s = {i if i!='panda' else 'beb' for i in names}
# print(s)