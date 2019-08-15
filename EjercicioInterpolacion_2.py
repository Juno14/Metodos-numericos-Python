from Interpolacion import *
x = [2, 4, 6]
f = [3.7, 4.1, 5.6]
a = lagrage(x, f, 3)
f = [4.2, 5.3, 6.7]
b = lagrage(x, f, 3)
f = [5.8, 6.1, 7.4]
c = lagrage(x, f, 3)
f = [7.1, 7.9, 8.2]
d = lagrage(x, f, 3)
y = [5, 10, 15, 20]
f = [a, b, c, d]
p = lagrage(y, f, 12)
print(p)
