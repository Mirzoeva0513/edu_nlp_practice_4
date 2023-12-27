"""
Реализуйте методы класса Complex так, чтобы экземпляры этого класса
поддерживали 4 арифметические операции (сложение, вычитание, умножение,
деление) и приведение к строке (примеры: 2+3i, -3-4i, 0+10i, 3+0i).

Арифметические операции должны поддерживать встроенные типы float и int,
к примеру выражение Complex(1, 2) + 2 должно возвращать результат Complex(3, 2).
"""


class Complex:
    """Custom implementation of a complex number."""

    ### ваше решение: ###
x = Complex(1, 2)
y = Complex(3, 4)

x == y

print(x + y)  # Вывод: 4+6i
print(x - y)  # Вывод: -2-2i
print(x * y)  # Вывод: -5+10i
print(x / y)  # Вывод: 0.44+0.08i
    

    ### конец решения ###
