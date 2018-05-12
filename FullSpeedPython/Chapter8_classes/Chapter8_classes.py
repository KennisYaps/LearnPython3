class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return abs(self.y2-self.y1)

    def height(self):
        return abs(self.x2-self.x1)

# [Note]: Methods may call other methods by using method attributes of the `self` argument:
    def area(self):
        return self.width() * self.height()

    def circumference(self):
        return(2 * self.width() + 2 * self.height())

    def __str__(self):
        return "({x1},{y1}) ({x2},{y2})".format(x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y2)


rectangle1 = Rectangle(1, 2, 3, -4)
rectangle2 = Rectangle(-9, 1, -4, 5)
# [Note]: print(rectangle1.width) = you are printing the method and what Python gives you is the method type (bound) + instance type to which it belongs + address of the instance. (eg. rectangle1 & rectangle2 have DIFF address)
# print(rectangle1.width) => <bound method Reactangle.width of <__main__.Reactangle object at 0x109179d30>>
# Thus, to invoke the method, add ()
print(rectangle1.width())
print(rectangle2.height())
print(rectangle1.area())
print(rectangle1.circumference())
print(rectangle1)
