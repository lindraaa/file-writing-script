file = open("try.txt" , "a")
file.write("new line!" )
file.close()

file = open("try.txt","r")
print(file.read())
