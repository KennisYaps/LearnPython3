# [List]
# [Qns 1: Using list slicing get the sublists [4, 9] and [10, 23].]
l = [1, 4, 9, 10, 23]
slice_1 = l[1: 3]    # [Note]: Return a new list of the requested element
slice_2 = l[3:]

# [Qns 2: Append the value 90 to the end of the list “l”. Check the difference between list concatenation and the “append” method.]
l.append(90)
print(l)

# [Qns 3: Calculate the average value of all values on the list. You can use the “sum” and “len” functions.]
a = [1, 2, 3]


def averageValueInAList(l):
    return sum(l)/len(l)


averageValueInAList(l)

# [Qns 4: Remove the sublist [4, 9].]
l[1:3] = []

# [List comprehension]
# [Qns 1: Using list comprehensions, create a list with the squares of the first 10 numbers.]
squares = [pow(element, 2) for element in range(10)]

# [Qns 2: Using list comprehensions, create a list with the cubes of the first 20 numbers.]
cubes = [pow(element, 3) for element in range(20)]

# [Qns 3: Create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.]
even = [i for i in range(20) if i % 2 == 0]
odd = [i for i in range(20) if i % 2 != 0]

# [Qns 4: Create a list with the squares of the even numbers from 0 to 20, and sum the list using the “sum” function. The result should be 1140. First create the list using list comprehensions, check the result, then apply the sum to the list comprehension.]

l1 = [pow(element, 2) for element in range(20) if element % 2 == 0]
sumOfl1 = sum(l1)
print(l1)

# [Qns 5: Make a list comprehension that returns a list with the squares of all even numbers from 0 to 20, but ignore those numbers that are divisible by 3. In other words, each number should be divisible by 2 and not divisible by 3. Search for the “and” keyword in the Python documentation. The resulting list is [4, 16, 64, 100, 196, 256].]
l2 = [pow(element, 2)
      for element in range(20) if (element % 2 == 0 and element % 3 != 0)]

