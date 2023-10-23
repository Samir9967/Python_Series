# num = [i*i for i in range(0,11)]
# print(num)

names = ['samir','maharana','aditi','ghadi','sum']
# expected output = ]['s','m','a','g']

l = [i for i in names if 'a' in i]
print(l)

# l = [i  if i !='samir' else 'sam' for i in  names]
# print(l)

                                   # creation of matrix using list comprehension
# l = [[j for j in range(3)] for i in range(3)]
# print(l)