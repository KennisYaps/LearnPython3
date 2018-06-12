# Qns : find rare characters in the mess below
import operator
import urllib.request
import re


def tabulate(text):
    tabulate = dict()
    for char in list(text):
        # setting the key
        tabulate[char] = tabulate.get(char, 0)+1
    return tabulate


def sortInAccendingOrder(d):
    sort = sorted(d.items(), key=operator.itemgetter(1))
    return sort


def grouped(arr):
    group = dict()
    for key, value in arr:
        # setting the value
        group.setdefault(value, []).append(key)
    return group


def getRareElement(text):
    t = tabulate(text)
    s = sortInAccendingOrder(t)
    g = grouped(s)
    convertToString = ''.join(g[1])
    print(convertToString)
    return convertToString


# Loading Data
# Method 1
input = open("challenge_2.txt").read()
getRareElement(input)

# Extract the text from HTML directly
# [Step 1: Load raw html source coding using urllib.request]
html = urllib.request.urlopen(
    "http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

# [step 2: Extract the comment blocks in html. Note that by default dot does not match \n, so we need to use re .DOTALL]
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
# OR
# comments = re.findall("<!--([\w\n]*?)-->", html)

# [step 3: The pattern <!--(.*)--> will capture all blocks inside <!-- and -->. We only care about the last part, so]
data = comments[-1]
getRareElement(data)
