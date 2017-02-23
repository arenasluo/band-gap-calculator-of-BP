import matplotlib.pyplot as plt
import numpy
import math
import sys
import random

global a,b,c,d,e,f

c=float(raw_input('y1: '))
print 'y1= ',c
print '                         '
d=float(raw_input('y2: '))
print 'y2= ',d
print '                         '

e=float(raw_input('strain range [-4,4], x1: '))/100
print 'x1= ',e
print '                         '

f=float(raw_input('strain range [-4,4], x2: '))/100
print 'x2= ',f
print '                         '


a=float((c-d)/(e-f))
print 'slope a=',a
print '                         '
b=float(c-a*e)
print 'intersection b=',b