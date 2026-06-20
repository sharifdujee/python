import math as m
x = int(input(" Enter First Number Number"))
y = int(input("Enter Second Number"))
n = 100.85

sum = x +y
sub =  x - y
multi = x * y
div = x / y
mod = x // y
root = x ** y
floor = m.floor(n)
sling = m.ceil(n)
print(f"The summation of Number {x} and Number {y} is {sum}")
print(f"The subtraction of Number {x} and Number {y} is {sub}")
print(f"The Multipication of Number {x} and Number {y} is {multi}")
print(f"The Division of Number {x} and Number {y} is {div}")
print(f"The Modules of Number {x} and Number {y} is {mod}")
print(f"The root of Number {x} and Number {y} is {root}")
print(f"The floor of Number {n}  is {floor}")
print(f"The Celling of Number {n}  is {sling}")

