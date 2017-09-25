import os

with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myfile:
# read() readline() readlines()

    print(myfile.read())

print(myfile.closed)

print(myfile.name)

print(myfile.mode)

os.rename("mydata.txt", "mydata2.txt")

os.remove("mydata2.txt")

# os.mkdir("mydir")

os.chdir("mydir")

print("current directory:", os.getcwd())

os.chdir("..")

print("current directory:", os.getcwd())

os.rmdir("mydir")