                               # add()
# s = {12,34,56,78,90}
# s.add("samir")
# print(s)

                                # update()
# s = {1,2,3,4,5}
# t = ['sam',12,34,1,2]
# l = (12,23,45,True,False)
# s.update(t,l,range(1,21))
# print(s)
# print(len(s))

                               #remove()
# s = {1,2,3,4,5,6}
# s.remove(5)
# print(s)

                                  # discard()
# s = {1,2,3,4,5,6}
# s.discard(78)
# print(s)

                                    # pop()
# s = {1,2,3,4,5,6}
# s.pop()
# print(s)

                                     # copy()
# s = {1,2,3,4}
# s1 = s.copy()
# print(s1)
# print(id(s),id(s1))

                                     # clear()
# s = {1,2,3,4,5}
# s.clear()
# print(s)

                                     # union()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6,7,9,10}
# c = a.union(b)
# print(c)

                                   #intersection()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6,7,9,10}
# c = a.intersection(b)
# print(c)

                                      # difference()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6,7,9,10}
# c = a.difference(b)
# print(c)

                                    #   symmetric_differennce()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6,7,9,10}
# c = a.symmetric_difference(b)
# print(c)

                                      # issubset()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6,7,9,10}
# c = b.issubset(a)
# print(c)

                                     # issuperset()
# a = {1,2,3,4,5,6}
# b = {1,2,5,6}
# c = a.issuperset(b)
# print(c)

                                    # isdisjoint()
a = {1,2,3,4,5,6}
b = {7,9,10}
print(a.isdisjoint(b))

