# Importing Time module to check time complexity
import time

# Importing os module to be used for file path extraction
import os

# Initiating time
Time = time.time()

# Considering a directory to search for txt files in this location
fileDirectory = "D:\\KOVIDH KUMAR D S\\KOVIDH KUMAR D S PYTHON\\PRACTICE2023\\AccelerateProject\\txtFiles"

# Creating a list to store the generated file paths
filePaths = []

# Generating the different txt file paths using os module
for (path, folders, files) in os.walk(fileDirectory):
    filesPath = [
        os.path.join(path, file)
        for file in files
    ]
    filePaths.extend(filesPath)


# Pre processing the words to be searched which is stored in txt file

# Storing the file location of search words
searchFileLocation = "D:\\KOVIDH KUMAR D S\\KOVIDH KUMAR D S PYTHON\\PRACTICE2023\\AccelerateProject\\CODE\\SearchWords.txt"

# Opening file in read mode
searchFile = open(searchFileLocation, "r")

# Traversing search words from file
search = searchFile.readlines()

# Removing the '\n' in the extracted search words list
for lineNo in range ( len ( search ) - 1 ):
    search[lineNo] = search[lineNo][0:len(search[lineNo])-1]

# Generating final list of search words in proper format

# List for stroring the search words
finalSearchWords = []

# Splitting the words by space reference in between
for word in search:
    finalSearchWords.append(word.split(" "))

# Closing the SearchWords.txt file
searchFile.close()

# Pre processing the words to be searched in files

# Extracting content from each files found in the given directory
for file in filePaths:

    print("\n\nSearching in file location >> ", file)

    # Opening file in read mode
    toSearchFile = open(file, "r")

    # Extracting text data from a particualar selected file
    toSearchIn = toSearchFile.readlines()

    # Removing the '\n' in the extracted search words list
    for lineNo in range(len(toSearchIn) - 1):
        toSearchIn[lineNo] = toSearchIn[lineNo][0:len(toSearchIn[lineNo]) - 1]

    # List for stroring the search words
    finalToSearchIn = []

    # Splitting the words by space reference in between
    for word in toSearchIn:
        finalToSearchIn.append(word.split(" "))

    # Initiating the serach process

    # Picking each list in a list containing search words
    for searchList in finalSearchWords:

        # Initializing line number
        lineNumber = 1

        # Picking each word in the search list
        for searchWord in searchList:

            print("\tSearching for the word : ", searchWord)

            # Picking a line (list) from list of data to be searched in
            for toSearchList in finalToSearchIn:

                # Picking a word from toSearchList
                for toSearchInList in toSearchList:

                    # Checking if search element is same or not
                    if toSearchInList == searchWord:

                        # Printing found message
                        print("\t\tMatch found in line number : ", lineNumber)

                # Incrementing line number
                lineNumber += 1

    # Closing the SearchWords.txt file
    toSearchFile.close()

# Ending time count and calculating the total execution time
print("\nTotal time taken to search all words is : " + str(time.time() - Time) + " ms (milli-seconds)")

