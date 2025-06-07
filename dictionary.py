dic = {
    "Harry": "Human being",
    "Chammach": "Spoon in english"
}
print(dic["Harry"])
print(dic["Chammach"])

dict = {
    344:"Mili",
    45:"Khili",
    65:"Lappo",
    89:"Pappo",
}

# print(dict[344])

info = {'name':'Karan' , 'age':19 , 'eligible': True}
print(info)
# print(info['name'])
# print(info.get('eligible2'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
