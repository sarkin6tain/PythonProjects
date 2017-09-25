import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myfile:

    myfile.write("Some random text\nMore random text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myfile:

    lineNum = 1

    while True:

        line = myfile.readline()

        if not line:
            break

        print("line", lineNum, " : ", line, end="")

        lineNum +=1