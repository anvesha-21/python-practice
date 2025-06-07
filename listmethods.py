l = [45,32,100,1,2,4]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l)
print(l.count(1))
print(l)

m=l.copy()
m[0]=0
print(l)

l.insert(1,899)
print(l)

m=[900,1000,1100]
k = l+m
print(k)
# l.extend(m)
print(l)

