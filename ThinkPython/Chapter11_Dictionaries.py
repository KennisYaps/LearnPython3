# wordFile = open('word.txt', 'r+')
# toReadTheEntireContent = wordFile.read()
# print(toReadTheEntireContent)

# toReadByline = wordFile.readline()
# print(toReadByline)

# wordFile.write('\nThis is a test')
# wordFile.close()
# wordFile = open('word.txt', 'r')

wordFile = open('word.txt', 'r')
listOfWords = []
for line in wordFile:
    listOfWords.append(line)

print(listOfWords)

wordFile.close()
