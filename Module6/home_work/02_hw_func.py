# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    pass


def distance(x1, x2, y1, y2):
    dist_point = float(((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5)
    return dist_point


x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

AB = distance(x1, x2, y1, y2)
print("AB = ", AB)

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

BC = distance(x1, x2, y1, y2)
print("BC = ", BC)

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

CA = distance(x1, x2, y1, y2)
print("CA = ", CA)

nums = [AB, BC, CA]
if nums[0]==AB:
    print("Самый короткий отрезок: AB")
elif nums[0] == BC:
    print("Самый короткий отрезок: BC")
else:
    print("Самый короткий отрезок: CA")
