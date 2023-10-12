                              # index()
# tup1 = (12,23,12,32,45,32)
# print(tup1.index(32))

                                # count()
# print(tup1.count(32))

                             # min and max
# Max = max(tup1)
# print(Max)
# print(len(tup1))

                                  # sorted()
# tup2 = sorted(tup1)
# print(tup2)

# tup3 = sorted(tup1, reverse=True)
# print(tup3)

# tup4 = reversed(tup1)
# print(tup4)

tup1 = (12,23,12,32,45,32)
new_list = []

for i in reversed(tup1):
    new_list.append(i)

new_tup = tuple(new_list)
print(new_tup)