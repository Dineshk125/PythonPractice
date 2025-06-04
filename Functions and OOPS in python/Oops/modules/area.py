def circle(radius: float):
    area = 3.14 * radius * radius
    print(f"The area of circle is  = {area}")


def ractangle(length: float, breadth: float):
    area = length * breadth
    print(f"The area of ractangle is = {area}")


def triangle(base: float, height: float):
    area = 0.5 * base * height
    print(f"The area of triangle is ={area}")


if (
    __name__ == "__main__"
):  ## this is use for only for this python file, not when this file import in another file.

    circle(50.90)
    ractangle(34, 5)
    triangle(40, 20)
