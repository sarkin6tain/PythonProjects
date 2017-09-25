import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myfile:

    myfile.write("Some random text\nMore random text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myfile:

    lineNum = 1

    while True:

        line = myfile.readline()

        if not line:
            break
        print("line", lineNum)
       # split()
        wordList = line.split()

        # len()
        print("Number of Words :", len(wordList))

        # loop count characters in the list
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # divide characer count / len word list
        avgNumChars = charCount/len(wordList)

        print("Avg Word Lenghts : {:.2}".format(avgNumChars))

        lineNum +=1