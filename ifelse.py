# a = int(input("Enter your age :- "))
# print("Your age is :" , a)

# if(a>18):
#     print("You can drive.")
#     print("YES")
# else:
#     print("You cannot drive.")
#     print("NO")
#     print("mili")
#Conditinal Operator
#  > , < , >= , <= , == , !=

# print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)

# applePrice = 210
# budget = 200

# applePrice = int(input("Enter price of Apples in market: "))
# budget=int(input("Enter your budget : "))

applePrice = 10
budget = 200


if(budget - applePrice >  50 ):
    print("Alexa, add 1kg Apples to the cart.")
elif(budget - applePrice > 70):
    print("Its's ok you can buy.")
else:
    print("Alexa, do not add Apples to the cart.")