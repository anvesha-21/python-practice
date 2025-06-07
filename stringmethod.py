# Strings are immutable

a = "!!!Harry!!!!!  Anvesha !!!  Mili!!!!"
print(len(a))
print(a)
print(a.upper(),"upper")
print(a.lower(),"lower")
print(a.rstrip("!"),"rstrip")
print(a.replace("Harry" , "Mili"),"replace")
print(a.split(" "),"split") # list mai hota h ye split basically 



blogheading = "introduction tO MY subJect"
print(blogheading.capitalize(),"capitalize")  

string = "Welcome to the Console!!!"
print(string.center(50),"stringcenter")
print(a.count("!"),"count")
print(a.count("M")) #1
print(a.count("m")) #0


string = "Welcome to the Console!!!"
print(string.endswith("!!!"),"endswith")

string = "Welcome to the Console!!!"
print(string.endswith("a"),"endswith")

string = "Welcome to the Console!!!"
print(string.endswith("to" , 4 , 10),"endswith")

string = "Welcome to the Console!!!"
print(string.endswith("to" , 4 , 9),"endswith")

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"),"endswith")

str1 = "He's name is Dan. He is an honest man."
print(str1.find("the"),"endswith") #it will return -1 value if the word or letter is not fount in the string 

# str1 = "He's name is Dan. He is an honest man."
# print(str1.index("the")) #it will return error exception value if the word or letter is not fount in the string 

str1 = "WelcomeToTheSonsole"
print(str1.isalnum(),"isalnum") #anvesha bas pehechanne ke liye likha h 

str1 = "WelcomeToTheSonsole"
print(str1.isalpha(),"isalpha")

str1 = "WelcomeToTheSonsole12345"
print(str1.isalpha(),"isalpha")

str1 = "WelcomeToTheSonsole12345"
print(str1.islower(),"islower")

str1 = "welcome to my home"
print(str1.islower(),"islower")

str1 = "WelcomeToMyHome"
print(str1.islower(),"islower")
print(str1.lower())

str1 = "WelcomeToMyHome"
print(str1.isprintable(),"isprintable")

str1 = "WelcomeToMyHome\n\n\n\n"
print(str1.isprintable(),"isprintable")
print(str1)

str1 = "        "   #using spacebar
print(str1.isspace(),"isspace")

str1 = ""   #using spacebar
print(str1.isspace(),"isspace")

str1 = "World Health Organisation"
print(str1.istitle(),"istitle")

str1 = "WelcomeToMyHome"
print(str1.istitle(),"istitle")

str1 = "Welcome To My Home"
print(str1.isupper(),"isupper")
print(str1.upper())

str1 = "!!!WelcomeToMyHome"
print(str1.startswith("!!!" , 0 ,4),"startswith")

str1 = "WELCOME TO MY HOME"
print(str1.swapcase(),"swapcase")

str1 = "His name is dan. he is an honest man."
print(str1.title(),"title")

