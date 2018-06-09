import re
import operator
# [Qns 1: Write a function called sumall that takes any number of arguments and returns their sum.]


def sumall(*args):
    return sum([*args])


print("Qns 1: ", sumall(1, 2, 3, 4))


# [Qns 2: Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at]
def modifyString(input):
    tolower = input.lower()
    removeSpecialCharacterAndSpaces = re.sub(
        r'[^a-zA-Z0-9 ]', "", tolower).replace(" ", "")
    return removeSpecialCharacterAndSpaces


def tabulated(words):
    tabulate = dict()
    for letter in words:
        tabulate[letter] = tabulate.get(letter, 0)+1
    return tabulate


def sortDict(d, index):
    sort = sorted(d.items(), key=operator.itemgetter(index))
    return sort


def groupedDict(d):
    grouped = dict()
    for key, value in d.items():
        grouped.setdefault(value, []).append(key)
    sort_Grouped = sortDict(grouped, 0)
    return sort_Grouped


def most_frequent(s):
    modify_string = modifyString(s)
    tabulate = tabulated(modify_string)
    # [Note]: sorted_tabulate will be a list of tuples sorted by the second element in each tuple
    # Not Grouped
    # sort = sortDict(tabulate, 1)
    # [print(tup[0]) for tup in sort]

    # Grouped
    sort_grouped = groupedDict(tabulate)
    [print("Counted ", key, "in these letters:", value)
     for key, value in sort_grouped]

    return sort_grouped


input = """ Write a function called most frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. """

print("Qns 2:")
most_frequent(input)
