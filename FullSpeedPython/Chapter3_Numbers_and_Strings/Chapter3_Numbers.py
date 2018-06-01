# [Qns 2: Calculate the average of the following sequences of numbers: (2, 4), (4, 8, 9), (12, 14/6, 15)]

# [Qns 3: volume of a sphere is given by (4/3 * pi * rˆ3). Calculate the volume of a sphere of radius 5. ]

pi = 3.1415


def volumeOfSphere(radius):
    volume = 4/3 * pi * pow(radius, 3)
    return volume


print(volumeOfSphere(5))

# [Qns 4: Use the module operator (%) to check which of the following numbers is even or odd: (1, 5, 20, 60/7).]


def isEvenOrOdd(number):
    result = ["Even", "Odd"]
    return result[number % 2]


print(isEvenOrOdd(1))


