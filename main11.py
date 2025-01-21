import math
from abc import ABC, abstractmethod
class Shape(ABC):
"""
Абстрактный базовый класс для всех фигур.
Использует абстрактный метод area, который должен быть
реализован в дочерних классах.
"""
@abstractmethod
def area(self):
"""
Абстрактный метод для вычисления площади фигуры.
Должен быть реализован в каждом наследующем классе.
"""
pass
class Circle(Shape):
"""
Класс для представления круга, наследует от Shape.
"""
def __init__(self, radius):
"""
Инициализация круга с заданным радиусом.
"""
self.radius = radius
def area(self):
"""
Вычисление площади круга.
Формула: π * радиус^2
"""
return math.pi * self.radius ** 2
class Rectangle(Shape):
"""
Класс для представления прямоугольника, наследует от Shape.
"""
def __init__(self, width, height):
"""
Инициализация прямоугольника с заданной шириной и высотой.
"""
self.width = width
self.height = height
def area(self):
"""
Вычисление площади прямоугольника.
Формула: ширина * высота
"""
return self.width * self.height
class Triangle(Shape):
"""
Класс для представления треугольника, наследует от Shape.
"""
def __init__(self, base, height):
"""
Инициализация треугольника с заданной основой и высотой.
"""
self.base = base
self.height = height
def area(self):
"""
Вычисление площади треугольника.
Формула: 0.5 * основа * высота
"""
return 0.5 * self.base * self.height
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
# Попытка создания экземпляра абстрактного класса Shape (должно
вызвать ошибку)
try:
shape = Shape() # Ожидается ошибка
except TypeError as e:
print(f"Ошибка: {e}")
