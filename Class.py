class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def runs(self):
        print("{} the dog runs".format(self.name))

    def eats(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("getting the value of height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("plz enter an integer")

    @property
    def width(self):
        print("getting the value of height")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("plz enter an integer")

    def GetArea(self):
        return int(self.__height) * int(self.__width)


def main():
    Smart = Dog("Smart", 40, 32)
    Smart.bark()
    jack = Dog("Jack")
    jack.eats()
    
    aSquare = Square("6", "10")
    print("Height ", aSquare.height)
    print("Width ", aSquare.width)
    print("A,  The area is =", aSquare.GetArea())
    
    bSquare = Square()
    bSquare.height = input("Enter a height: ")
    bSquare.width = input("Enter a width: ")

    print("Height ", bSquare.height)
    print("Width ", bSquare.width)
    print("B, The area is =", bSquare.GetArea())



main()
