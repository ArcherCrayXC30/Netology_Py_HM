import math

print("task_6 ----->")


def circle_square():
    radius = int(input("Радиус круга:"))
    square = math.pi * (radius ** 2)
    print("Площадь круга: ", square)
    pass


def triangle_square():
    line_a = int(input("Длина стороны А:"))
    line_b = int(input("Длина стороны B:"))
    line_c = int(input("Длина стороны C:"))
    half_per = (line_a + line_b + line_c) / 2
    square = math.sqrt(half_per*(half_per - line_a)*(half_per - line_b)*(half_per - line_c))
    print("Площадь треугольника: ", square)
    pass


def rectangle_square():
    line_a = int(input("Длина стороны А:"))
    line_b = int(input("Длина стороны B:"))
    square = line_a * line_b
    print("Площадь прямоугольника: ", square)

areas_calc = {
    'круг': circle_square,
    'треугольник': triangle_square,
    'прямоугольник': rectangle_square

}

type_figure = input("Введите тип фигуры (круг, треугольник, прямоугольник): ")

areas_calc[type_figure]()