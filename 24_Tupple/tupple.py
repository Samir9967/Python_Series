                                     # creation of empty tuple
tup = ()
# print(type(tup), tup)

                                    # creation of single value 
tup2 = (23)               # without comma
# print(type(tup2),tup2)          # it will give int without comma
tup3 = (23,)               # with comma
# print(type(tup3),tup3)

                     # creation of tuple with different datatypes of values
tup4 = (1,2,"samir",True,12.45,[2,3,4])
# print(tup4)

                     # creation of tuple without ()
tup5 = 10,20,30,[10,20],"samir",False,12.34
# print(type(tup5),tup5)

                         #creation of range with raange()
# tup5 = tuple(range(1,10))
# print(tup5)

tup6 = "Maharana"
l = tuple(tup6)
# print(type(l),l)

                               # Accesssing tuple element by indexing
# print(tup4[5])   # by positive index
# print(tup4[-3])  # by negative index

                                 # Accessing by slicing
# print(tup5[2:])

                                   # basic mathematical operation on tuple
                          # Concatenation of list 
# l = (10,20,30)
# s = (40,30)
# p  = l + s
# print(p)

                          # repitition of tuple
# l = (10,20,30)
# s = l * 2
# print(s)

