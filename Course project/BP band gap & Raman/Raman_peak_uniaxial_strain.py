# Uniaxial strain 
import matplotlib.pyplot as plt
import numpy
import math
import sys
import random

global arstr

#armchair strain, 'ars': armchair strain  
arstr=float(raw_input('Please input armchair strain: '))

#print arstr
#Ag1
if arstr>=-4 and arstr<=-2:
    Ag1=float((-150)*(arstr/100)+366)
    print 'Ag1 peak position: ',Ag1,' cm-1'
    
if arstr>-2 and arstr<=0:
    Ag1=float((-50)*(arstr/100)+368)
    print 'Ag1 peak position: ',Ag1,' cm-1'    
    
if arstr>0 and arstr<=2:
    Ag1=float((-350)*(arstr/100)+368)
    print 'Ag1 peak position: ',Ag1,' cm-1'    
    
if arstr>2 and arstr<=4:
    Ag1=float((-400)*(arstr/100)+369)
    print 'Ag1 peak position: ',Ag1,' cm-1'   
    
#Ag2
if arstr>=-4 and arstr<=-2:
    Ag2=float((350)*(arstr/100)+456)
    print 'Ag2 peak position: ',Ag2,'cm-1' 
    
if arstr>-2 and arstr<=0:
    Ag2=float((350)*(arstr/100)+456)
    print 'Ag2 peak position: ',Ag2,'cm-1' 
    
if arstr>0 and arstr<=2:
    Ag2=float((100)*(arstr/100)+456)
    print 'Ag2 peak position: ',Ag2,'cm-1' 
    
if arstr>2 and arstr<=4:
    Ag2=float((100)*(arstr/100)+456)
    print 'Ag2 peak position: ',Ag2,'cm-1' 
    
#B2g
if arstr>=-4 and arstr<=-2:
    B2g=float((300)*(arstr/100)+432)
    print 'B2g peak position: ',B2g,'cm-1' 
    
if arstr>-2 and arstr<=0:
    B2g=float((450)*(arstr/100)+433)
    print 'B2g peak position: ',B2g,'cm-1' 
    
if arstr>0 and arstr<=2:
    B2g=float((200)*(arstr/100)+433)
    print 'B2g peak position: ',B2g,'cm-1' 
    
if arstr>2 and arstr<=4:
    B2g=float((100)*(arstr/100)+435)
    print 'B2g peak position: ',B2g,'cm-1' 
    
#    
#    
m=[]
r=[]
n=0
while n<401:
	l=300+0.5*n
	r.append(l)
	if l<Ag1:
		m.append(0)
		n=n+1
	if l==Ag1:
		m.append(5)
		n=n+1
	if l>Ag1 and l<B2g:
		m.append(0)
		n=n+1
	if l==B2g:
		m.append(3.5)
		n=n+1
	if l>B2g and l<Ag2:
		m.append(0)
		n=n+1
	if l==Ag2:
		m.append(5.4)
		n=n+1
	if l>Ag2:
		m.append(0)
		n=n+1

plt.plot(r,m,'r')
plt.grid(True)
plt.xlabel('Raman frequency (cm-1)')
plt.ylabel('Intensity')
plt.text(Ag1-2,5,float(Ag1),color='blue',fontsize=10)
plt.text(B2g-2,3.5,float(B2g),color='blue',fontsize=10)
plt.text(Ag2-2,5.4,float(Ag2),color='blue',fontsize=10)
plt.show()
