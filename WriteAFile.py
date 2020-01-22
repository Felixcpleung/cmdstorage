example2 = "C:/users/felix/desktop/Python Ex/example2.txt"
with open(example2,"w") as file2:
    file2.write("This is line A\n")
    file2.write("This is line B\n")
    file2.closed   
    
#check whether it work
with open(example2, 'r') as file1:
    print(file1.read())
    file1.closed
    
#append
with open(example2,'a') as file2:
    file2.write("This is line C\n")
    file2.write("This is line D\n")
    file2.closed 
    
with open(example2, 'r') as file1:
    print(file1.read())
    file1.closed


list1= ["I\n", "love\n", "you\n"]
list1

#write strings in a list to a file
example3 = "C:/users/felix/desktop/Python Ex/example3.txt"
list1= ["I\n", "love\n", "you\n"]
list1
with open(example3, 'w') as writefile:
    for line in list1:
        print (line)
        writefile.write(line)


example3 = "C:/users/felix/desktop/Python Ex/example3.txt"
list1= ["first\n", "second\n"]
list1
with open(example3, 'w') as writefile:
    for line in list1:
        print (line, end ="")
        writefile.write(line)