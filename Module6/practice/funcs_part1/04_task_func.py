# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    dist = ((x1 - x2)**2 + (y1 - y2)**2) * 0.5
    return dist

p1 = distance(10, 14, 12, 18)
p2 = distance(14, 12, 18, 12)
p3 = distance(10, 12, 12, 12)

def can_triangle(p1, p2, p3):
    if (p1 + p2) > p3 and (p1 + p3) > p1 and (p2 + p3) > p1 and (p1 > 0, p2 > 0, p3 > 0):
        print("Possible")
    else:
        print("Impossible")


can_triangle(p1, p2, p3)


# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
