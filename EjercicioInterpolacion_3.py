import pylab as pl
def f(t):
    return t**3 - 11*t**2 + 37*t -33
t = pl.arange(2, 5.1, 0.1)
pl.plot(t, f(t))
x = [2, 3, 4, 5]
y = [5, 6, 3, 2]
pl.plot(x, y, 'o')
pl.grid(True)
pl.show()
