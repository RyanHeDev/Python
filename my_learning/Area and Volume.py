# Area and Volume 

def area(lenght, width):
    return lenght * width


def perimeter(lenght, width):
    return lenght + width + lenght + lenght


def volume(lenght, width, height):
    return lenght * width * height


def surfaceArea(lenght, width, height):
    return (lenght * width * 2) + (lenght * height * 2) + (width * height * 2)


print(area(10, 10))

print(area(0, 9999))

print(area(5, 8))

print(perimeter(10, 10))

print(perimeter(0, 9999))

print(perimeter(5, 8))

print(volume(10, 10, 10))

print(volume(9999, 0, 9999))

print(volume(5, 8, 10))

print(surfaceArea(10, 10, 10))

print(surfaceArea(9999, 0, 9999))

print(surfaceArea(5, 8, 10))

