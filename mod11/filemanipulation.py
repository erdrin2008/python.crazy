line=["hello world!\n","welcome to python\n"]
with open("examples.txt","w") as file: #we open the file with permissions to write
    file.writelines(lines) #we write on multiple lines