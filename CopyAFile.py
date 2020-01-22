#file to being copied"
example2 = "C:/users/felix/desktop/Python Ex/example2.txt"

#file acquiring content from example2
example4 = "C:/users/felix/desktop/Python Ex/example2.txt"

print("content on example2.txt")
with open(example2,'r') as readfile:
    print(readfile.read())

with open(example2,'r')as readfile:
    with open(example4,"w") as writefile:
        writefile.write(readfile.read())

print ("content on example4.txt")
with open(example4,'r') as readfile:
    print(readfile.read())


1
2
3
4