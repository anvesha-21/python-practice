# s = {2,5,2,7}
# print(s)


# info = {"mili" , 20 , True , 5.6 , 20  }
# print(info)

# mili = set()
# print (type(mili))

# for value in info:
#     print(value)


sets method

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1 , s2)
s1.update(s2)


cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid" } 

cities3 = cities.union(cities2)
cities3 = cities.intersection(cities2)
cities.intersection_update(cities2)
cities3 = cities.symmetric_difference(cities2)
cities.symmetric_difference_update


cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid" } 
print(cities.isdisjoint(cities2))

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities2 = { "Seoul" , "Kabul"  } 
print(cities.issuperset(cities2))
cities3 = {"Tokyo" , "Madrid" , "Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities.add("Helsinki")
print(cities)

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Helsinki" , "Warsaw" , "Seoul"}
cities.update(cities2)
print(cities)

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
# cities.remove("Tokyo2")  through error
cities.discard("Tokyo2")  #dosen't through error
print(cities)

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
del cities
print(cities)

cities = {"Tokyo" ,  "Madrid" , "Berlin" , "Delhi"}
cities.clear()
print(cities)

# info = {"mile" , 20 , True , 5.6 , 20  }
# if "mili" in info:
#     print("Mili is there")
# else:
#     print("Mili is not there")
