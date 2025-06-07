tup =(1 ,)     
tup = (1,2,45,67,345,78 , "mili" , True)
print(type(tup),tup)

print(tup[0])
print(tup[3])
print(tup[-5])
print(tup[2])
# print(tup[45])


if 342 in tup:
    print("YES, 345 is present in tuple...")


tup2=tup[1:4]
print(tup2)


countries = ("India","America","Nepal","Russia","USA","UK","UAE")
temp=list(countries)
temp.append("Russia")              #add
temp.pop(3)                        #remove item
temp[2]="London"                   #change item
countries=tuple(temp)
print(countries)

res = countries.count("India")
print(res)

res1 = countries.index("India")
print(res1)


tuple1 = (0,3,4,5,6,2,5,0,6,4,2,54,3,212,4,4,6,8,5,3,5,5,5,6,7,5,3)
res2 = tuple1.index( 5,5,12)
print(res2)
res3 = len(tuple1)
print(res3)