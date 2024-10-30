from networkx.algorithms.threshold import triangles


def calc_area_triangle(b,h):
    area=0.5*b*h
    print("The area of the triangle is",area)

b=float(input("Enter the base"))
h=float(input("Enter the height"))


calc_area_triangle(b,h)

triangles=[[8,9],[6,7],[21,27]]

for t in triangles:
    calc_area_triangle(t[0],t[1])

