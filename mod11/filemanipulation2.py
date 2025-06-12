import os
if os.path.exists("example.text"):
 print("file exist😎😎")

 name="alice"
 age=15

 with open("output,txt","w") as file:
     file.write("name:"+name+"\n")
     file.write("age:"+str(age)+"\n")