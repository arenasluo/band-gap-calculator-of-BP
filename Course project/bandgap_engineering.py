import matplotlib.pyplot as plt
import numpy
import math
import sys
import random

pi=math.pi
global l,m,n,k,r,aa,bb,cc,dd

e0=-8.6288
e1=3.507
e2=0.411
print '                                            '
print 'For undeformed SLBP, we find that the bandgap Egap = 1.6 eV;'
print '                                            '
print ' ex and ey are normal strains'
print '                                            '
print ' Phai is the direction of mechanical strain '
print '                                            '
print ' *****1. For in-plain uniaxial strain: '
print '                                            '
print ' Please set ex!=0 and ey=0, or ex=0 and ey!=0 '
print '                                            '
print '                                            '
print ' ****************************************** '
print '                                            '
print ' *****2. For in-plane biaxial strain:****** '
print '                                            '
print ' *******  Please set ex=ey=e, ez=0  ******* '
print '                                            '
print '                                            '
print ' ****************************************** '
print '                                            '
print ' *****3. For a general in-plain strain: ****** '
print '                                            '
print ' Please set For a general in-plain strain with ex!=ey, ez=0'
print '                                            '
def e(): #e
    global r
    r=float(raw_input('Please input e,the value should be at the range [-4,4]:'))/100
    print '                                            '
    if (r>=-4) & (r<=4):
        print 'e',r
        return 1
    else:
        print 'wrong input data'
        return 0
       

    
#ex
def ex(): #ex
    global m
    m=float(raw_input('Please input ex, the value should be at the range [-4,4]:'))/100
    print '                                            '
    if (m>=-4) & (m<=4):
        print 'ex',m
        return 1
    else:
        print 'wrong input data'
        return 0
    
while True: 
    if ex()==0:
        ex()
    else:
        break

#ey    
def ey(): #ey
    global l
    l=float(raw_input('Please input ey, the value should be at the range [-4,4]:'))/100
    print '                                            '
    if (l>=-4) & (l<=4):
        print 'ey',l
        return 1
    else:
        print 'wrong input data'
        return 0    
while True: 
    if ey()==0:
        ey()
    else:
        break   

#ez
#def ez(): #ez
#    global n
#    n=float(raw_input('Please input ez, the value should be at the range [-4,4]:'))/100
#    if (n>=-1) & (n<=1):
#        print 'ez',n
#        return 1
#    else:
#        print 'wrong input data'
#        return 0    
#while True: 
#    if ez()==0:
#        ez()
#    else:
#        break    

#gama
#def gama(): #gama
#    global k
#    k=float(raw_input('Please input gama, the value should be at the range [-1,1]:'))
#    if (k>=-1) & (k<=1):
#        print 'gama',k
#        return 1
#    else:
#        print 'wrong input data'
#        return 0    
#while True: 
#    if gama()==0:
#        gama()
#    else:
#        break
    
def phai():
    global phai_paprameter
    p=float(raw_input('Please input phai, the direction of mechanical strain,and we suggest put in with integer 0 or 1:'))
    print '                                            '
    phai_paprameter=p*(math.pi)/2

#def deltaEgap_case1():
#    global deltaEgap_1
#    deltaEgap_1=float(e0)*n
    
def deltaEgap_case2():
    global deltaEgap_2
    deltaEgap_2=(float(e1)-float(e2))*m-2*float(e2)*m*math.cos(2*phai_paprameter)

def deltaEgap_case3():
    global deltaEgap_3
    deltaEgap_3=2*(float(e1)-2*(float(e2)))*r
    
def deltaEgap_case4():
    global deltaEgap_4
    deltaEgap_4=(float(e1)-2*(float(e2)))*(m+l)-2*(float(e2))*(m-l)*(math.cos(2*phai_paprameter))
    
#def deltaEgap_case5():
#    global deltaEgap_5
#    deltaEgap_5=44*(e2)*k*math.sin(2*phai_paprameter)
    
#def deltaEgap_case6():
#    global deltaEgap_6
#    deltaEgap_6=(float(e1)-2*float((e2)))*(m)+2*float(e2)*math.sqrt((m)**2+(2*float(k))**2)

#m: ex 
#l: ey    
#gama: k:
#n: ez
#
#
#Case 1
#if m==0 and l==0 and n!=0 and k==0:#	For uniaxial strain in the z direction
#    print 'uniaxial strain in the z direction'
#    deltaEgap_case1()  
#    print 'delta_Egap1:',deltaEgap_1,' eV'
    
#Case 2: in-plain uniaxial strain
if m!=0 and l==0: #and n==0:# and k==0:
    print 'in-plain uniaxial strain!!!!'
    print '                                            '
    phai()
    deltaEgap_case2()
    aa=round(deltaEgap_2,3)
    print 'delta_Egap2:',aa,' eV'
    print '                                            '
   

#Case 2: in-plain uniaxial strain
elif m==0 and l!=0:# and n==0:# and k==0:
    print 'in-plain uniaxial strain!!!!'
    print '                                            '
    phai()
    deltaEgap_case2()
    bb=round(deltaEgap_2,3)
    print 'delta_Egap2:',bb,' eV'
    print '                                            '

#Case 3: for in-plane biaxial strain
elif m==l: # and n==0:# and k==0:
    while True: 
        if e()==0:
            e()
        else:
            break        
    print 'in-plain biaxial strain!!!!'
    print '                                            '
    deltaEgap_case3()
    cc=round(deltaEgap_3,3)
    print 'delta_Egap3:',cc,' eV'
    print '                                            '

#Case 4: for a general in-plain strain 
elif m!=l :#and n==0:# and k==0: 
    print 'a general in-plain strain!!!!'
    print '                                            '
    phai()
    deltaEgap_case4()
    dd=round(deltaEgap_4,3)
    print 'delta_Egap4:',dd,'eV'
    print '                                            '

#Case 5: pure shear strain
#elif m==0 and l==0 and n==0 and k!=0: #with shear strain
#    print 'pure shear strain'
#    phai()
#    deltaEgap_case5()    
#    t=math.sin(2*phai_paprameter)
#    print 'delta_Egap5:',deltaEgap_5,'eV'

#Case 6: simultaneously apply the uniaxial strain and the shear strain
#elif l==0 and n==0 and m!=0 and k!=0: #with shear strain
#    print 'simultaneously apply the uniaxial strain and the shear strain'
#    deltaEgap_case6()  
#   print 'delta_Egap6:',deltaEgap_6,'eV'
#

    