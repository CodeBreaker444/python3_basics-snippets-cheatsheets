import os
file=open("test.txt","wb")
print(file.mode)
print(file.name)
file.write(bytes("Hello i am ready\n",'UTF-8'))
file.close()
file=open("test.txt","r+")
print(file.read())
#os.remove("test.txt")