#Biseccion
def funcion(x):
        y = x-math.sin(x)
        return y
#Entradas
x0 = 1
x1 = 10
i = 0
ERROR = 10
while ERROR > 1**-8:
    x2 = (x0 + x1) / 2
    fx0 = funcion(x0)
    fx2 = funcion(x2)
    if fx2 == 0:
        raiz = x2
        break
    elif fx0 * fx2 < 0:
        x1 = x2
    else:
        x0 = x2
    raiz = x2
    i = i + 1
    ERROR = abs(fx2)
print('Iteracion:',i,'Raiz aproximada:',raiz)
#Newton-Raphson
import math
def f(x):
     return Tu funcion
def der(x):
     return Su derivada
i = 1
x0 = ?
for r in range (1, ?):
         x1 = x0 - f(x0)/der(x0)
         x0 = x1
print(x0)
