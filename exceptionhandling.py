# a = input("Enter a number:")
# print(f"Multiplication table of {a} is:")

# try:
#    for i in range(1 , 11):
#       print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#    print("Invalid Input! ")


# print("Some imp lines of codes")
# print("End of program")


try:
   num=int(input("Enter an integer:"))
   a=[6,3]
   print(a[num])
except ValueError:
   print("Number entered is not an integer. ")
except IndexError:
   print("Index error")
