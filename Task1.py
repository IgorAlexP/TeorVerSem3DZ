"""Задача1
Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
среднее квадратичное отклонение, 
смещенную и несмещенную оценки дисперсий для данной выборки."""

import math

# Значения выборки
values = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Среднее арифметическое
mean = sum(values) / len(values)
print(f"Среднее арифметическое: {mean}")

# Отклонения от среднего значения
deviations = [x - mean for x in values]

# Квадрат отклонений
squares = [x ** 2 for x in deviations]

# Смещенная оценка дисперсии
variance_biased = sum(squares) / len(values)
print(f"Смещенная оценка дисперсии: {variance_biased}")

# Несмещенная оценка дисперсии
variance_unbiased = sum(squares) / (len(values) - 1)
print(f"Несмещенная оценка дисперсии: {variance_unbiased}")

# Среднее квадратичное отклонение
standard_deviation = math.sqrt(variance_unbiased)
print(f"Среднее квадратичное отклонение: {standard_deviation}")