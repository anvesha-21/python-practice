letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Mili"

print (letter.format(name,country))
print(f"Hey my name is {name} and i am from {country}")
print(f"We ar representing f-string over here: Hey my name is {{name}} and i am from {{country}}")

price=49.0999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format(price=49.0999))

print(type(f"{2*30}"))
