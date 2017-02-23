import matplotlib.pyplot as plt
import numpy
x=numpy.arange(0,0.4,0.01)
def a(x):                            # c11
    return 165.8-37.3*x

def b(x):                            # c12
    return 63.9-15.6*x

def c(x):                            # c44  
    return 79.6-12.8*x

def d(x):                            # s11
    return (a(x)+b(x))/(a(x)**2+a(x)*b(x)-2*((b(x))**2))

def e(x):                            # s12
    return (b(x)*(-1))/(a(x)**2+a(x)*b(x)-2*((b(x))**2))

def f(x):                            # s44
    return 1/c(x)
    
def g(x):                            # E100
    return 1/d(x)

def h(x):                            # E110
    return 1/(d(x)-0.5*((d(x)-e(x))-0.5*f(x)))

def i(x):                            # E111
    return 1/(d(x)-float(2)/float(3)*((d(x)-e(x))-0.5*f(x)))

def j(x):
    return (g(x)+h(x)+i(x))/3

plt.plot(x,j(x),'r')
plt.grid(True)
plt.show()


