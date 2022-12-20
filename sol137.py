# Area of a Triangle
def tri_area(base, height):
    return base * height / 2

base = input('What is the base of the triangle? ')
height = input('What is the height of the triangle? ')

print(tri_area(base, height))