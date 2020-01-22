example1 = "C:/users/felix/desktop/Python Ex/example1.txt"
with open(example1,"r") as file1:
    print("%r" %(file1.read(4)))
    print("%r" %(file1.read(4)))
    print("%r" %(file1.read(7)))
    print("%r" %(file1.read(15)))


with open(example1,'r') as file1:
    print("The first line is" + file1.readline())
    
    
with open(example1,'r') as file1:
    Fileaslist = file1.readlines()
    print(file1.read())
    
    
    