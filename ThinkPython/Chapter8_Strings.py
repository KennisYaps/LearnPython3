# [Qns 1: Write a function that takes a string as an argument and displays the letters backward, one per line]


def displayLettersBackwards(str):
    index = len(str)-1
    while index < len(str) and index >= 0:
        print(str[index])
        index -= 1


displayLettersBackwards("hello")


# [Qns 2: Modify the program to fix this error.]

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter+'u'+suffix)
    else:
        print(letter + suffix)

# [Qns 3: Given that fruit is a string, what does fruit[:] mean?]
s = "fruit"
print(s[:])  # fruit

# [Qns 4: Modify `find` so that it has a third parameter, the index in word where it should start looking.]


def find(word, letter, index):
    indexToFindFrom = index
    while indexToFindFrom < len(word):
        if word[indexToFindFrom] == letter:
            return indexToFindFrom
        else:
            indexToFindFrom += 1
    return False


print(find("hello", "o", 1))

# [Qns 5: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.]


def count(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    print("Total count for " + letter + " in " + word + " is " + str(count))
    return count


count("hellokajshfie", "l")

# [Qns 7: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of as in 'banana'.]

s = "banana"
print("Total a in banana", s.count("a"))
