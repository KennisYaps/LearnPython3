s = "abc"
# [Qns 1a: Use a function to get the length of the string.]
print(len(s))
# [Qns 1b: Write the necessary sequence of operations to transform the string “abc” in “aaabbbccc”. ]


def transformString(str):
    result = ""
    i = 0
    while (i < len(str)):
        result += str[i]*3
        i += 1
    return result


print(transformString("abc"))

# [Qns 2a: Use a function that allows you to find the first occurence of “b” in the string, and the first occurence of “ccc”.]
s = transformString("abc")
b_index = s.find("b")
ccc_index = s.find("ccc")
# [Qns 2b: Use a function that allows you to replace all occurences of “a” to “X”, and then use the same function to change only the first occurence of “a” to “X”.]
replace_all_a = s.replace("a", "X")
replace_a = s.replace("a", "X", 1)
print(replace_all_a)
print(replace_a)


