# with open ('myfile2.txt' , 'r') as f:
#     print(type(f))
#     # Move to the 10th byte of the file
#     f.seek(10)
#     # Read the next 5 bytes
#     print(f.tell())
#     data  = f.read(5)
#     print(data)

with open ('myfile2.txt' , 'w') as f:
    f.write('Hello World!')
    # f.truncate(5)


with open ('myfile2.txt' , 'r') as f:
    print(f.read())