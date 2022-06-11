import math

def angles(n):
     degree = ((n-2)*180)/n
     degree = format(degree, "0.3f")
     return degree

def area(length, n):
    apothem = length/(2 * math.tan(math.pi/n))
    perimeter = n * length
    area = (apothem * perimeter) / 2 
    area = format(area, "0.3f")
    
    return area


def main():

    userInput = int(input("\nHow many sides does your polygon have: "))
    print("Your polygon with", userInput, "sides will have", angles(userInput), "degree interior angles")
    

    userInput2 = int(input("\nWhat is the length of the sides of your polygon: "))
    print("The area of your polygon is", area(userInput2, userInput), "units squared\n")


main()
