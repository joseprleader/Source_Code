# Intercollegiate Programming Competition Blue Track 2021
# Challenge 8 It Adds Up

def main():
    numbersString = input("Enter the desired sum, number of elements, each element: ")
    numbersString = numbersString.split()
    desiredSum = int(numbersString[0])
    numberOfElements = int(numbersString[1])
    numbers = [int(x) for x in numbersString[2:]]
    for i in range(numberOfElements):
        for j in range(i + 1, numberOfElements):
            if numbers[i] + numbers[j] == desiredSum:
                pair = Pair(numbers[i], numbers[j], numbers)
    if not Pair.registry:
        print("No pairs found")
    else:
        for p in Pair.registry:
            print(str(p) + " found at " + p.getCoordinates())


# We create a class with all the necessary methods to find the pairs
class Pair:
    registry = []

    def __init__(self, first, second, list):
        self.list = list
        self.first = first
        self.second = second
        self.registry.append(self)

    def __str__(self):
        return "(" + str(self.first) + ", " + str(self.second) + ")"

    def __repr__(self):
        return str(self)

    def getFirst(self):
        return self.first

    def getSecond(self):
        return self.second

    def getCoordinates(self):
        return "[" + str(self.list.index(self.first) + 1) + "][" + str(self.list.index(self.second) + 1) + "]"

    def getFirstCoordinate(self):
        return self.list.index(self.first)

    def getSecondCoordinate(self):
        return self.list.index(self.second)

main()