import sys
import re

isnatural = True
with open(sys.argv[1], "r") as file:
    data = file.readline().strip()  # Считываем строку из файла
coordinates = re.findall("[-+]?\d+\.\d+|[-+]?\d+", data)
del coordinates[10]
del coordinates[0]
coordinates = [float(i) for i in coordinates]
for i in coordinates:
    if i < 0:
        isnatural = False
        print("Kоординаты не могут быть отрицательными")
# преобразуем в числовой тип данных
'''Воспользуемся 3-м признаком подобия треугольников: Если три стороны одного треугольника пропорциональны трем сторонам другого треугольника, то треугольники подобны
'''


# Функция расчитывающая длины по координатам
def lenght(X1, Y1, Z1, X2, Y2, Z2):
    lenght = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2 + (Z2 - Z1) ** 2) ** 0.5
    return lenght


# Функция определения подобия треугольников
def issimilar():
    AB1 = lenght(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5])
    BC1 = lenght(coordinates[3], coordinates[4], coordinates[5], coordinates[6], coordinates[7], coordinates[8])
    AC1 = lenght(coordinates[0], coordinates[1], coordinates[2], coordinates[6], coordinates[7], coordinates[8])
    AB2 = lenght(coordinates[9], coordinates[10], coordinates[11], coordinates[12], coordinates[13], coordinates[14])
    BC2 = lenght(coordinates[12], coordinates[13], coordinates[14], coordinates[15], coordinates[16], coordinates[17])
    AC2 = lenght(coordinates[9], coordinates[10], coordinates[11], coordinates[15], coordinates[16], coordinates[17])
    if AB1 / AB2 == BC1 / BC2 and BC1 / BC2 == AC1 / AC2 and AB1 / AB2 == AC1 / AC2:
        print("Треугольника подобны")
    else:
        print("Треугольники не подобны")


if isnatural:
    issimilar()
