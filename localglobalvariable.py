# x = 4
# print(x)

# def hello():
#     x = 5
#     y =1
#     print(f"The Local x is {x}")   
#     print("Hello Harry")

#     print(f"The Global x is {x}")



# hello()

# print(f"The Global x is {x}")
#     # print(y) Can't print y because y is local variable so it can't be print outside the function


x = 10 #Global Variable

def my_function():
    global x
    x = 4
    y=5 #local variable
    print(y)

my_function()
print(x)
print(x)
# print(y)