# f = open ('myfile2.txt' , 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line , type(line))
#         break


# f = open ('myfile2.txt' , 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# f = open ('myfile2.txt' , 'r')
# i = 0
# while True:
#     i = i + 1 
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of students {i} in Maths is:{m1*2}")
#     print(f"Marks of students {i} in English is:{m2*2}")
#     print(f"Marks of students {i} in SST is:{m3*2}")
#     print(line)


f=open('myfile2.txt' , 'w')
lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
f.writelines(lines)
f.close