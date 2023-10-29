s = "mama"
d = {}
for i in s:
    d[i] = d.get(i,0)+1
print(d)
        