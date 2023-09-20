                                        #without break statement
for i in range(1,11,1):
    print(i)
else:
    print("End loop")

                                           #with break statemet
for i in range(1,11,1):
    if i == 5:
        break
    print(i)
else:
    print("end")