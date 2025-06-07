# def average(a=12 , b=2):
#     print("The average is", (a+b)/2) 

# # average(4 , 6)
# average(b=9)

# average(a=21) 


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)

c=average(5,6,7,1)
print(c)
# average (5,6,7)

# # default arguments...
# def name(fname,mname = "Vitthal", lname="Chaturvedi"):
#     print("HEYY!!!",fname,mname,lname)

# name("Anvesha" , "Vitthal" , "Chaturvedi")       


# Keywords arguments...

def name (**name):
    print(type(name))
    print("Hello" , name["fname"],name["mname"],name["lname"])
name(mname="Vitthal",lname="Chaturvedi",fname="Anvesha")
