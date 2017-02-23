import matplotlib.pyplot as plt
import numpy
import math
import sys
import random
from decimal import Decimal

#To mention that, round function will lose accuracy
#from decimal import Decimal


pi=math.pi
global l,m,n,k,r,x,y,Ag1,B2g,x,y,Ag2

#linear interpolation
pi=math.pi
global l,m,n,k,r,aa,bb,cc,dd,p

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
    if (r>=-0.04) & (r<=0.04):
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
    if (m>=-0.04) & (m<=0.04):
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
    if (l>=-0.04) & (l<=0.04):
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
    global phai_paprameter,p
    p=float(raw_input('Please input phai (0 or 0.5 or 1,corresponding to cos0, cospai/2, cospai), the direction of mechanical strain: '))
    print '1.for uniaxial strain case: if you input 1, you can get uniaxial stain only in zigzag(y) direction '
    print '                                            '
    print 'if you input 0, you can get uniaxial strain only in armchair(x) direction; '
    print '                                            '
    print '2. for other cases We also suggest input in with integer 0 or 1'
    print '                                            '
    phai_paprameter=2*p*(math.pi)/2

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
print 'm=:',m
#Case 2: in-plain uniaxial strain;ex!=0, ey==0
if m!=0 and l==0: #and n==0:# and k==0:
    global deltaEgap_2,pp,aa
    print 'in-plain uniaxial strain!!!!'
    print '                                            '
    phai() # input phai
    deltaEgap_case2() # calculate band gap change
    print 'p=',p
    if p==1 :
        print 'uniaxial strain in zigzag(y) direction'
        #zigzag strain, 'zigstr': zigstr strain  
        #
        #
        zigstr=m
	print 'zigstr=',zigstr
        
        #Ag1
        if zigstr>=-0.04 and zigstr<=-0.02:
            Ag1=format(float((100)*(zigstr/100)+364),'.2f')
	    print 'Ag1 peak position: ',Ag1,' cm-1'
            
        if zigstr>-0.02 and zigstr<=0:
            Ag1=format(float((300)*(zigstr/100)+368),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'    
            
        if zigstr>0 and zigstr<=0.02:
            Ag1=format(float((-100)*(zigstr/100)+368),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'    
            
        if zigstr>0.02 and zigstr<=0.04:
            Ag1=format(float((-100)*(zigstr/100)+368),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'   

        #B2g
        if zigstr>=-0.04 and zigstr<=-0.02:
            B2g=format(float((-750)*(zigstr/100)+430),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
        if zigstr>-0.02 and zigstr<=0:
            B2g=format(float((-600)*(zigstr/100)+433),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
        if zigstr>0 and zigstr<=0.02:
            B2g=format(float((-900)*(zigstr/100)+433),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
            
        if zigstr>0.02 and zigstr<=0.04:
            B2g=format(float((-1250)*(zigstr/100)+440),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 

            
        #Ag2
        if zigstr>=-0.04 and zigstr<=-0.02:
            Ag2=format(float((-500)*(zigstr/100)+455),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if zigstr>-0.02 and zigstr<=0:
            Ag2=format(float((-450)*(zigstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if zigstr>0 and zigstr<=0.02:
            Ag2=format(float((-800)*(zigstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if zigstr>0.02 and zigstr<=0.04:
            Ag2=format(float((-250)*(zigstr/100)+445),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
        s=[]
	r=[]
	n=0
	while n<20001:
	    l=format(300+0.01*n,'.2f')
	    r.append(l)
	    if l<Ag1:
		s.append(0)
		n=n+1
	    if l==Ag1:
		s.append(5)
		n=n+1
		
	    if l>Ag1 and l<B2g:
		s.append(0)
		n=n+1
	    if l==B2g:
		s.append(3.5)
		n=n+1
		
	    if l>B2g and l<Ag2:
		s.append(0)
		n=n+1
		
	    if l==Ag2:
		s.append(5.4)
		n=n+1
		
	    if l>Ag2:
		s.append(0)
		
		n=n+1
	plt.plot(r,s,'r')
	plt.grid(True)
	plt.xlabel('Raman frequency (cm-1)')
	plt.ylabel('Intensity')
	deltaEgap_2=round(deltaEgap_2,3)
	#plt.text(450,6.0,'uniaxial strain in zigzag_y_direction',color='black',fontsize=10)
	plt.text(400,5.8,deltaEgap_2,color='blue',fontsize=10)
	plt.text(370,5.8,'delta_Egap2:',color='blue',fontsize=10)
	plt.text(420,5.8,'eV:',color='blue',fontsize=10)	
	plt.text(Ag1,5,Ag1,color='blue',fontsize=10)
	plt.text(B2g,3.5,B2g,color='blue',fontsize=10)
	plt.text(Ag2,5.4,Ag2,color='blue',fontsize=10)
	plt.show()	

    pp=round(deltaEgap_2,3)
    print '                                            '
    print 'delta_Egap2:',pp,' eV'
    print '                                            '
    
    if p==0.5:
	    print 'uniaxial strain in zigzag(y) direction'
	    #zigzag strain, 'zigstr': zigstr strain  
	    #
	    #
	    zigstr=m
	    print 'zigstr=',zigstr
	    
	    #Ag1
	    if zigstr>=-0.04 and zigstr<=-0.02:
		Ag1=format(float((100)*(zigstr/100)+364),'.2f')
		print 'Ag1 peak position: ',Ag1,' cm-1'
		
	    if zigstr>-0.02 and zigstr<=0:
		Ag1=format(float((300)*(zigstr/100)+368),'.2f')
		print 'Ag1 peak position: ',Ag1,' cm-1'    
		
	    if zigstr>0 and zigstr<=0.02:
		Ag1=format(float((-100)*(zigstr/100)+368),'.2f')
		print 'Ag1 peak position: ',Ag1,' cm-1'    
		
	    if zigstr>0.02 and zigstr<=0.04:
		Ag1=format(float((-100)*(zigstr/100)+368),'.2f')
		print 'Ag1 peak position: ',Ag1,' cm-1'   
    
	    #B2g
	    if zigstr>=-0.04 and zigstr<=-0.02:
		B2g=format(float((-750)*(zigstr/100)+430),'.2f')
		print 'B2g peak position: ',B2g,'cm-1' 
		
	    if zigstr>-0.02 and zigstr<=0:
		B2g=format(float((-600)*(zigstr/100)+433),'.2f')
		print 'B2g peak position: ',B2g,'cm-1' 
		
	    if zigstr>0 and zigstr<=0.02:
		B2g=format(float((-900)*(zigstr/100)+433),'.2f')
		print 'B2g peak position: ',B2g,'cm-1' 
		
		
	    if zigstr>0.02 and zigstr<=0.04:
		B2g=format(float((-1250)*(zigstr/100)+440),'.2f')
		print 'B2g peak position: ',B2g,'cm-1' 
    
		
	    #Ag2
	    if zigstr>=-0.04 and zigstr<=-0.02:
		Ag2=format(float((-500)*(zigstr/100)+455),'.2f')
		print 'Ag2 peak position: ',Ag2,'cm-1' 
		
	    if zigstr>-0.02 and zigstr<=0:
		Ag2=format(float((-450)*(zigstr/100)+456),'.2f')
		print 'Ag2 peak position: ',Ag2,'cm-1' 
		
	    if zigstr>0 and zigstr<=0.02:
		Ag2=format(float((-800)*(zigstr/100)+456),'.2f')
		print 'Ag2 peak position: ',Ag2,'cm-1' 
		
	    if zigstr>0.02 and zigstr<=0.04:
		Ag2=format(float((-250)*(zigstr/100)+445),'.2f')
		print 'Ag2 peak position: ',Ag2,'cm-1' 
	    s=[]
	    r=[]
	    n=0
	    while n<20001:
		l=format(300+0.01*n,'.2f')
		r.append(l)
		if l<Ag1:
		    s.append(0)
		    n=n+1
		if l==Ag1:
		    s.append(5)
		    n=n+1
		    
		if l>Ag1 and l<B2g:
		    s.append(0)
		    n=n+1
		if l==B2g:
		    s.append(3.5)
		    n=n+1
		    
		if l>B2g and l<Ag2:
		    s.append(0)
		    n=n+1
		    
		if l==Ag2:
		    s.append(5.4)
		    n=n+1
		    
		if l>Ag2:
		    s.append(0)
		    
		    n=n+1
	    plt.plot(r,s,'r')
	    plt.grid(True)
	    plt.xlabel('Raman frequency (cm-1)')
	    plt.ylabel('Intensity')
	    deltaEgap_2=round(deltaEgap_2,3)
	    #plt.text(450,6.0,'uniaxial strain in zigzag_y_direction',color='black',fontsize=10)
	    plt.text(400,5.8,deltaEgap_2,color='blue',fontsize=10)
	    plt.text(370,5.8,'delta_Egap2:',color='blue',fontsize=10)
	    plt.text(420,5.8,'eV:',color='blue',fontsize=10)	
	    plt.text(Ag1,5,Ag1,color='blue',fontsize=10)
	    plt.text(B2g,3.5,B2g,color='blue',fontsize=10)
	    plt.text(Ag2,5.4,Ag2,color='blue',fontsize=10)
	    plt.show()	
	    

     
    if p==0:
        print 'uniaxial strain in armchair(x) direction'
        #armchair strain, 'ars': armchair strain  
        #arstr=float(raw_input('Please input armchair strain: '))
        arstr=m
        #print arstr
        #Ag1
        if arstr>=-0.04 and arstr<=-0.02:
            Ag1=format(float((-150)*(arstr/100)+366),'.2f')	    
            print 'Ag1 peak position: ',Ag1,' cm-1'
            
        if arstr>-0.02 and arstr<=0:
            Ag1=format(float((-50)*(arstr/100)+368),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'    
            
        if arstr>0 and arstr<=0.02:
            Ag1=format(float((-350)*(arstr/100)+368),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'    
            
        if arstr>0.02 and arstr<=0.04:
            Ag1=format(float((-400)*(arstr/100)+369),'.2f')
            print 'Ag1 peak position: ',Ag1,' cm-1'   
            
        #Ag2
        if arstr>=-0.04 and arstr<=-0.02:
            Ag2=format(float((350)*(arstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if arstr>-0.02 and arstr<=0:
            Ag2=format(float((350)*(arstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if arstr>0 and arstr<=0.02:
            Ag2=format(float((100)*(arstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        if arstr>0.02 and arstr<=0.04:
            Ag2=format(float((100)*(arstr/100)+456),'.2f')
            print 'Ag2 peak position: ',Ag2,'cm-1' 
            
        #B2g
        if arstr>=-0.04 and arstr<=-0.02:
            B2g=format(float((300)*(arstr/100)+432),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
        if arstr>-0.02 and arstr<=0:
            B2g=format(float((450)*(arstr/100)+433),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
        if arstr>0 and arstr<=0.02:
            B2g=format(float((200)*(arstr/100)+433),'.2f')
            print 'B2g peak position: ',B2g,'cm-1' 
            
        if arstr>0.02 and arstr<=0.04:
            B2g=format(float((100)*(arstr/100)+435),'.2f')
	    print 'B2g peak position: ',B2g,'cm-1' 
	s=[]
	r=[]
	n=0
	while n<20001:
	    l=format(300+0.01*n,'.2f')
	    r.append(l)
	    if l<Ag1:
		s.append(0)
		n=n+1
	    if l==Ag1:
		s.append(5)
		n=n+1
	    if l>Ag1 and l<B2g:
		s.append(0)
		n=n+1
	    if l==B2g:
		s.append(3.5)
		n=n+1
	    if l>B2g and l<Ag2:
		s.append(0)
		n=n+1
	    if l==Ag2:
		s.append(5.4)
		n=n+1
	    if l>Ag2:
		s.append(0)
		n=n+1
	plt.plot(r,s,'r')
	plt.grid(True)
	plt.xlabel('Raman frequency (cm-1)')
	plt.ylabel('Intensity')
	deltaEgap_2=round(deltaEgap_2,3)
	plt.text(400,5.8,deltaEgap_2,color='blue',fontsize=10)
	#plt.text(450,6.0,'uniaxial strain in armchair_x_direction',color='blue',fontsize=10)
	plt.text(370,5.8,'delta_Egap2:',color='blue',fontsize=10)
	plt.text(420,5.8,'eV:',color='blue',fontsize=10)	
	plt.text(Ag1,5,Ag1,color='blue',fontsize=10)
	plt.text(B2g,3.5,B2g,color='blue',fontsize=10)
	plt.text(Ag2,5.4,Ag2,color='blue',fontsize=10)
	plt.show()
	
    aa=round(deltaEgap_2,3)
    print '                                            '
    print 'delta_Egap2:',aa,' eV'
    print '                                            '
   

#Case 2: in-plain uniaxial strain
#elif m==0 and l!=0:# and n==0:# and k==0:
#    print 'in-plain uniaxial strain!!!!'
#    print '                                            '
#    phai()
#    deltaEgap_case2()
#    bb=round(deltaEgap_2,3)
#    print 'delta_Egap2:',bb,' eV'
#    print '                                            '

#Case 3: for in-plane biaxial strain
#m: ex 
#l: ey    
#gama: k:
#n: ez
elif m==l: # and n==0:# and k==0:
    global deltaEgap_3
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
    x=m*100
    y=l*100    
    ##############################################################################
    ##############################################################################
    ##############################       Ag1      ################################	
    ##############################################################################	
    ##############################################################################
    #############################
    #Raman range [346] boundary
    #############################	
    if x==4 and y==4:
	    Ag1=346
	    print 'Ag1 peak position: ',Ag1,' cm-1'
			    
    ##########################
    #Raman range [350 to 346] 
    ##########################	
    if x>=3.5 and x<4 and y<4 and y>2.1: 
	    if y>float((4+2.1)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.1)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<=4 and y>2.8 and x>=3 and x<3.5: 
	    if y>float((4+2.8)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.8)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<=4 and y>3.4 and x>=2.5 and x<3: 
	    if y>float((3.4+4)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+4)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    if y<=4 and y>3.8 and x>=2.5 and x<3: 
	    if y>float((4+3.8)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.8)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
		    
    ##########################
    #Raman range [354 to 350] 
    ##########################	
    if y<=2.1 and y>=0.4 and x>=3.5 and x<4: 
	    if y>float((0.4+2.1)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.4+2.1)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<=2.8 and y>=1.1 and x>=3 and x<3.5: 
	    if y>float((1.8+1.1)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8+1.1)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<=3.4 and y>=1.8 and x>=2.5 and x<3: 
	    if y>float((2.4+1.8)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4+1.8)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    if y<=3.8 and y>=2.4 and x>=2 and x<2.5: 
	    if y>float((2.8+2.4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+2.4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=2.8 and x>=0.5 and x<2: 
	    if y>float((2.8+4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<=4 and y>=3.4 and x>=0 and x<0.5: 
	    if y>float((3.4+4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=3.6 and x>=-0.5 and x<0: 
	    if y>float((4+3.6)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((4+3.6)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=3.9 and x>=-0.7 and x<-0.5: 
	    if y>float((4+3.9)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((4+3.9)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y==4 and x==-0.7:
	    Ag1=354
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
	    
    ##########################
    #Raman range [358 to 354] 
    ##########################
    if y<0.4 and y>=-1.2 and x>=3.5 and x<4: 
	    if y>float((0.4-1.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.4-2.1)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    
    if y<1.1 and y>=-0.6 and x>=3 and x<3.5: 
	    if y>float((1.1-0.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.1-0.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.8 and y>=-0.1 and x>=2.5 and x<3: 
	    if y>float((1.8-0.1)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8-0.1)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.4 and y>=0.6 and x>=2 and x<2.5: 
	    if y>float((2.4+0.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4+0.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.8 and y>=1.4 and x>=0.5 and x<2: 
	    if y>float((2.8+1.4)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+1.4)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.4 and y>=2.2 and x>=0 and x<0.5: 
	    if y>float((3.4+2.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+2.2)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.6 and y>=2.3 and x>=-0.5 and x<0: 
	    if y>float((3.6+2.3)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.6+2.3)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.6 and x>=-0.7 and x<-0.5: 
	    if y>float((4+2.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.9 and x>=-1 and x<-0.7: 
	    if y>float((4+2.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<4 and y>=2.9 and x>=-1.5 and x<-1: 
	    if y>float((4+2.9)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.9)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.2 and x>=-2 and x<-1.5: 
	    if y>float((4+3.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.2)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.5 and x>=-2.5 and x<-2: 
	    if y>float((4+3.5)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.5)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.7 and x>=-3.3 and x<-2.5: 
	    if y>float((4+3.7)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.7)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if x==-3.3 and y==4:
	    Ag1=358
	    print 'Ag1 peak position: ',Ag1,' cm-1'		
    ##########################
    #Raman range [362 to 358] 
    ##########################
    if y<-1.2 and y>=-3.2 and x>=3.5 and x<4: 
	    if y>float((-3.2-1.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((-3.2-1.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.6 and y>=-2.2 and x>=3 and x<3.5: 
	    if y>float((-0.6-2.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.6-2.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.1 and y>=-1.6 and x>=2.5 and x<3: 
	    if y>float((-0.1-1.6)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.1-1.6)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.6 and y>=-1 and x>=2 and x<2.5: 
	    if y>float((0.6-1)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.6-1)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.4 and y>=-0.5 and x>=1.5 and x<2: 
	    if y>float((1.4-0.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.4-0.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.9 and y>=0.2 and x>=1 and x<1.5: 
	    if y>float((1.9+0.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.9+0.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.05 and y>=0.8 and x>=0.5 and x<1: 
	    if y>float((2.05+0.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.05+0.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.2 and y>=0.8 and x>=0  and x<0.5: 
	    if y>float((2.2+0.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.2+0.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.3 and y>=1.3 and x>=-0.5  and x<0: 
	    if y>float((2.3+1.3)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.3+1.3)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.6 and y>=1.5 and x>=-1  and x<-0.5: 
	    if y>float((2.6+1.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.6+1.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.9 and y>=1.7 and x>=-1.5  and x<-1: 
	    if y>float((2.9+1.7)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.9+1.7)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.2 and y>=1.8 and x>=-2  and x<-1.5: 
	    if y>float((3.2+1.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.2+1.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.5 and y>=2.1 and x>=-2.5  and x<-2: 
	    if y>float((3.5+2.1)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.5+2.1)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.7 and y>=2.3 and x>=-3.3  and x<-2.5: 
	    if y>float((3.7+2.3)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.7+2.3)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.45 and x>=-3.5  and x<-3.3: 
	    if y>float((4+2.45)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.45)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.5 and x>=-4  and x<-3.5: 
	    if y>float((4+2.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    ##########################
    #Raman range [366 to 362] 
    ##########################	
    if x==-4 and y==4:
	    Ag1=360
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
    if x==4 and y==-4:
	    Ag1=364
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
	    
    if y<-3.2 and y>=-4 and x>=3.6  and x<4: 
	    if y>float((-4-3.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.2 and y>=-3.8 and x>=3.5  and x<3.6: 
	    if y>float((-3.8-2.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.8-2.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.2 and y>=-3.8 and x>=3  and x<3.5: 
	    if y>float((-3.8-2.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.8-2.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.6 and y>=-3.1 and x>=2.5  and x<3: 
	    if y>float((-1.6-3.1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-1.6-3.1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1 and y>=-2.4 and x>=2  and x<2.5: 
	    if y>float((-2.4-1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.4-1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.5 and y>=-1.9 and x>=1.5  and x<2: 
	    if y>float((-0.5-1.9)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.5-1.9)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<0.2 and y>=-1.4 and x>=1  and x<1.5: 
	    if y>float((0.2-1.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.2-1.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.8 and y>=-0.8 and x>=0.5  and x<1: 
	    if y>float((0.8-0.8)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.8-0.8)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.2 and y>=0 and x>=0  and x<0.5: 
	    if y>float((1.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.2)/2):
		    if x==0 and y==0:
			    Ag1=368
			    print 'Ag1 peak position: ',Ag1,' cm-1'
		    elif x!=0 and y!=0:
			    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.3 and y>=0.4 and x>=-0.5  and x<0: 
	    if y>float((1.3-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.3-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.5 and y>=0.5 and x>=-1 and x<-0.5: 
	    if y>float((1.5-0.5)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.5-0.5)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.7 and y>=0.5 and x>=-1.5 and x<-1: 
	    if y>float((1.7-0.5)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.7-0.5)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.8 and y>=0.4 and x>=-2 and x<-1.5: 
	    if y>float((1.8-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.1 and y>=0.2 and x>=-2.5 and x<-2: 
	    if y>float((2.1-0.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.1-0.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.3 and y>=0.1 and x>=-3 and x<-2.5: 
	    if y>float((2.3-0.1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.3-0.1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.35 and y>=-0.05 and x>=-3.5 and x<-3: 
	    if y>float((2.4-0.05)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4-0.05)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.4 and y>=-0.4 and x>=-4 and x<-3.5: 
	    if y>float((2.4-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    ##########################
    #Raman range [370 to 366] 
    ##########################
    if y<-3.1 and y>=-4 and x>=3 and x<3.6: 
	    if y>float((-4-3.1)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.1)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.4 and y>=-4 and x>=2.4 and x<3: 
	    if y>float((-2.4-4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.4-4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-1.9 and x>=2 and x<2.4: 
	    if y>float((-3.5-1.9)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-1.9)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-1.9 and x>=1.5 and x<2: 
	    if y>float((-3.5-1.9)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-1.9)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.4 and y>=-3.1 and x>=1.0 and x<1.5: 
	    if y>float((-3.1-1.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.1-1.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.8 and y>=-2.8 and x>=0.5 and x<1: 
	    if y>float((-2.8-0.8)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.8-0.8)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0 and y>=-2.5 and x>=0 and x<0.5: 
	    if y>float((-2.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.4 and y>=-2.1 and x>=-0.5 and x<=0: 
	    if y>float((-2.1-0.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.1-0.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.5 and y>=-1.1 and x>=-1 and x<-0.5: 
	    if y>float((-1.1-0.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-1.1-0.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.5 and y>=-0.8 and x>=-1.5 and x<-1: 
	    if y>float((-0.8-0.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.8-0.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<0.4 and y>=-0.8 and x>=-2 and x<-1.5: 
	    if y>float((-0.8-0.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.8-0.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.2 and y>=-1 and x>=-2.5 and x<-2: 
	    if y>float((0.2-1)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.2-1)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.1 and y>=-1.2 and x>=-3 and x<-2.5: 
	    if y>float((0.1-1.2)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.1-1.2)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.05 and y>=-2 and x>=-3.5 and x<-3: 
	    if y>float((0.1-1.2)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.1-1.2)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.4 and y>=-2.4 and x>-4 and x<-3.5: 
	    if y>float((-0.4-2.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.4-2.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if x==-4 and y==-1.2:
	    Ag1=366
	    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if x==-4 and y==-2.6:
	    Ag1=370
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    ##########################
    #Raman range [374 to 370] 
    ##########################
    if y<-3.5 and y>=-4 and x>=2 and x<2.4: 
	    if y>float((-4-3.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.5)/2):
		    Ag1=371
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<-3.5 and y>=-4 and x>=0.5 and x<2: 
	    if y>float((-4-3.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.5)/2):
		    Ag1=371
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.5 and y>=-4 and x>=-0.5 and x<0.5: 
	    if y>float((-4-2.5)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-2.5)/2):
		    Ag1=372
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.1 and y>=-4 and x>=-2 and x<-0.5: 
	    if y>float((-4-1.1)/2):
		    Ag1=float((371+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-1.1)/2):
		    Ag1=373
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1 and y>=-4 and x>=-2.7 and x<-2: 
	    if y>float((-4-1)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-1)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2 and y>=-3.7 and x>=-3 and x<-2.7: 
	    if y>float((-3.7-2)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.7-2)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.4 and y>=-3.4 and x>=-3.5 and x<-3: 
	    if y>float((-3.4-2.4)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.4-2.4)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.6 and y>=-3.3 and x>=-4 and x<-3.5: 
	    if y>float((-3.3-2.6)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.3-2.6)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    #############################
    #Raman range [378] boundary
    #############################		
    if y<-3.7 and y>=-4 and x>=-3 and x<-2.7: 
	    if y>float((-3.7-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.7-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-4 and x>=-3.5 and x<-3: 
	    if y>float((-3.5-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.4 and y>=-4 and x>=-4 and x<-3.5: 
	    if y>float((-3.4-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.4-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    
    
    
    ##############################################################################
    ##############################################################################
    ##############################       B2g      ################################	
    ##############################################################################	
    ##############################################################################
    
    
    
    ##########################
    #Raman range [465]
    ##########################
    if x==-4 and y>=-4 and y<=4:
	    B2g=465; # at the left boundary
	    print 'B2g peak position: ',B2g,' cm-1'
    
    
    ##########################
    #Raman range [465 to 456]
    ##########################	
    if x>-4 and x<-3.5 and y<=4 and y>3.5: # I set the mesh for 0.25, -3.5
	    if x>-3.75:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.75:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.45 and y>3 and y<=3.5: # I set the mesh for 0.275, -3.45 
	    if x>-3.725:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.725:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.4 and y>2.5 and y<=3: # I set the mesh for 0.3, -3.4
	    if x>-3.7:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.7:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.35 and y>2 and y<=2.5: # I set the mesh for 0.325, -3.35
	    if  x>-3.675:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.675:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.3 and y>1.5 and y<=2: # I set the mesh for 0.3, -3.3
	    if x>-3.65:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.65:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.25 and y>1 and y<=1.5: # I set the mesh for 0.375, -3.25 
	    if x>-3.625:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.625:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.2 and y>0.5 and y<=1: # I set the mesh for 0.4,-3.2 
	    if x>-3.6:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.6:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.15 and y>0 and y<=0.5: # I set the mesh for 0.425,-3.15
	    if x>-3.575:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.575:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.1 and y>-0.5 and y<=0: # I set the mesh for 0.45, -3.1
	    if x>-3.55:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.55:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.05 and y>-1 and y<=-0.5: # I set the mesh for 0.475, -3.05
	    if x>-3.525:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.525:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3 and y>-1.5 and y<=-1: # I set the mesh for 0.5, -3
	    if x>-3.5:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.5:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.9 and y>-2 and y<=-1.5: # I set the mesh for 0.55, -2.9
	    if x>-3.45:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.45:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.8 and y>-2.5 and y<=-2: # I set the mesh for 0.6, -2.8
	    if x>-3.4:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.4:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.75 and y>-3 and y<=-2.5: # I set the mesh for 0.625, -2.75
	    if x>-3.375:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.375:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.8 and y>-3.5 and y<=-3: # I set the mesh for 0.6, -2.8
	    if x>-3.4:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.4:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.85 and y>=-4 and y<=-3.5: # I set the mesh for 0.575, -2.85
	    if x>-3.425:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.425:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.9 and y==-4 : # I set the mesh for 0.55, -2.9
	    if x>-3.45:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.45:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [456 to 447]
    ##########################	
    if x>=-3.5 and x<-2.2 and y<=4 and y>3.5: 
	    if x>float((-3.5-2.2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.5-2.2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.45 and x<-2.15 and y>3 and y<=3.5: 
	    if x>float((-3.45-2.15)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.45-2.15)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.4 and x<-2.1 and y>2.5 and y<=3: 
	    if x>float((-3.4-2.1)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.4-2.1)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.35 and x<-2.05 and y>2 and y<=2.5: 
	    if  x>float((-3.35-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.35-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.3 and x<-2.05 and y>1.5 and y<=2: 
	    if x>float((-3.3-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.3-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.25 and x<-2.05 and y>1 and y<=1.5: 
	    if x>float((-3.25-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.25-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.2 and x<-2 and y>0.5 and y<=1:
	    if x>float((-3.2-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.2-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.15 and x<-2 and y>0 and y<=0.5: 
	    if x>float((-3.15-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<float((-3.15-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.1 and x<-2 and y>-0.5 and y<=0: 
	    if x>float((-3.1-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.1-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.05 and x<-1.9 and y>-1 and y<=-0.5: 
	    if x>float((-3.05-1.9)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.05-1.9)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3 and x<-1.8 and y>-1.5 and y<=-1: 
	    if x>float((-3-1.8)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3-1.8)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.9 and x<-1.7 and y>-2 and y<=-1.5: 
	    if x>float((-2.9-1.7)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.9-1.7)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.8 and x<-1.65 and y>-2.5 and y<=-2: 
	    if x>float((-2.8-1.65)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.8-1.65)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.75 and x<-1.66 and y>-3 and y<=-2.5: 
	    if x>float((-2.75-1.66)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.75-1.66)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.8 and x<-1.7 and y>-3.5 and y<=-3: 
	    if x>float((-2.8-1.7)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.8-1.7)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.85 and x<-1.75 and y>-4 and y<=-3.5: # I set the mesh for 0.625, -2.85
	    if x>float((-2.85-1.75)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.85-1.75)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
    
    if x>=-2.9 and x<-1.8 and y==-4: 
	    if x>float((-2.9-1.8)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.9-1.8)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'		
    ##########################		
    #Raman range [447 to 438]
    ##########################
    if x>=-2.2 and x<-1 and y<=4 and y>3.5: 
	    if x>float((-1-2.2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-1-2.2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.15 and x<-0.95 and y>3 and y<=3.5: 
	    if x>float((-0.95-2.15)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.15)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.1 and x<-0.95 and y>2.5 and y<=3: 
	    if x>float((-0.95-2.1)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.1)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.95 and y>2 and y<=2.5: 
	    if  x>float((-0.95-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.9 and y>1.5 and y<=2:
	    if x>float((-0.9-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.9-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.85 and y>1 and y<=1.5: 
	    if x>float((-0.85-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.85-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.8 and y>0.5 and y<=1: 
	    if x>float((-0.8-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.8-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.75 and y>0 and y<=0.5: 
	    if x>float((-0.75-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.15-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.7 and y>-0.5 and y<=0: 
	    if x>float((-0.7-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.9 and x<-0.6 and y>-1 and y<=-0.5: 
	    if x>float((-0.6-1.9)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.9)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.8 and x<-0.55 and y>-1.5 and y<=-1: 
	    if x>float((-0.55-1.8)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.55-1.8)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.7 and x<-0.6 and y>-2 and y<=-1.5: 
	    if x>float((-0.6-1.7)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.7)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.65 and x<-0.6 and y>-2.5 and y<=-2: 
	    if x>float((-0.6-1.65)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.65)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.66 and x<-0.6 and y>-3 and y<=-2.5: 
	    if x>float((-0.6-1.66)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.66)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.7 and x<-0.65 and y>-3.5 and y<=-3: 
	    if x>float((-0.65-1.7)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.65-1.7)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.75 and x<-0.7 and y>=-4 and y<=-3.5: 
	    if x>float((-0.7-1.75)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-1.75)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.8 and x<-0.75 and y==-4: 
	    if x>float((-0.75-1.8)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-1.8)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [438 to 428]
    ##########################
    if x>=-1 and x<0.35 and y<=4 and y>3.5: 
	    if x>float((-1-0.35)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-1-0.35)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>3 and y<=3.5: 
	    if x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>2.5 and y<=3: 
	    if x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>2 and y<=2.5: 
	    if  x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.9 and x<0.45 and y>1.5 and y<=2:
	    if x>float((-0.9-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.9-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.85 and x<0.5 and y>1 and y<=1.5: 
	    if x>float((-0.85-0.5)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.85-0.5)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.8 and x<0.55 and y>0.5 and y<=1: 
	    if x>float((-0.8-0.55)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.8-0.55)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.75 and x<0.6 and y>0 and y<=0.5: 
	    if x>float((-0.75-0.6)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-0.6)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.7 and x<0.6 and y>-0.5 and y<=0: 
	    if x>float((-0.7-0.6)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-0.6)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.55 and y>-1 and y<=-0.5: 
	    if x>float((-0.6-0.55)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.55)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.55 and x<0.5 and y>-1.5 and y<=-1: 
	    if x>float((-0.55-0.5)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.55-0.5)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.45 and y>-2 and y<=-1.5: 
	    if x>float((-0.6-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.4 and y>-2.5 and y<=-2: 
	    if x>float((-0.6-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.4 and y>-3 and y<=-2.5: 
	    if x>float((-0.6-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.65 and x<0.45 and y>-3.5 and y<=-3: 
	    if x>float((-0.65-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.65-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.7 and x<0.45 and y>=-4 and y<=-3.5: 
	    if x>float((-0.7-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.75 and x<0.45 and y==-4: 
	    if x>float((-0.75-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
    
		    
    ##########################		
    #Raman range [428 to 419]
    ##########################
    if x>=0.35 and x<1.3 and y<=4 and y>3.5: 
	    if x>float((1.3-0.35)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.35)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.35 and y>3 and y<=3.5: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.4 and y>2.5 and y<=3: 
	    if x>float((1.4-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.5 and y>2 and y<=2.5: 
	    if  x>float((1.4-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.6 and y>1.5 and y<=2:
	    if x>float((1.6-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.6-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.5 and x<1.55 and y>1 and y<=1.5: 
	    if x>float((1.55-0.5)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.55-0.5)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.55 and x<1.5 and y>0.5 and y<=1: 
	    if x>float((1.5-0.55)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.5-0.55)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.6 and x<1.5 and y>0 and y<=0.5: 
	    if x>float((1.5-0.6)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.5-0.6)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.6 and x<1.45 and y>-0.5 and y<=0: 
	    if x>float((1.45-0.6)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.45-0.6)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.55 and x<1.45 and y>-1 and y<=-0.5: 
	    if x>float((1.45-0.55)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.45-0.55)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.5 and x<1.4 and y>-1.5 and y<=-1: 
	    if x>float((1.4-0.5)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.5)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.4 and y>-2 and y<=-1.5: 
	    if x>float((1.4-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.35 and y>-2.5 and y<=-2: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.3 and y>-3 and y<=-2.5: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y>-3.5 and y<=-3: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y>=-4 and y<=-3.5: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y==-4: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [419 to 410]
    ##########################
    if x>=1.3 and x<2.3 and y<=4 and y>3.5: 
	    if x>float((2.3-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.35 and x<2.35 and y>3 and y<=3.5: 
	    if x>float((2.35-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.4 and y>2.5 and y<=3: 
	    if x>float((2.4-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.4-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.5 and y>2 and y<=2.5: 
	    if  x>float((2.5-1.5)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.5)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.6 and x<2.55 and y>1.5 and y<=2:
	    if x>float((2.55-1.6)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.55-1.6)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.55 and x<2.5 and y>1 and y<=1.5: 
	    if x>float((2.5-1.55)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.55)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.45 and y>0.5 and y<=1: 
	    if x>float((2.5-1.55)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.55)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.4 and y>0 and y<=0.5: 
	    if x>float((2.4-1.5)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.4-1.5)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.45 and x<2.35 and y>-0.5 and y<=0: 
	    if x>float((2.35-1.45)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.45)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.45 and x<2.35 and y>-1 and y<=-0.5: 
	    if x>float((2.35-1.45)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.45)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.3 and y>-1.5 and y<=-1: 
	    if x>float((2.3-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.3 and y>-2 and y<=-1.5: 
	    if x>float((2.3-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.35 and x<2.3 and y>-2.5 and y<=-2: 
	    if x>float((2.3-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.3 and y>-3 and y<=-2.5: 
	    if x>float((2.3-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.25 and y>-3.5 and y<=-3: 
	    if x>float((2.25-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.25-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.2 and y>=-4 and y<=-3.5: 
	    if x>float((2.2-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.2-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.2 and y==-4: 
	    if x>float((2.2-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.2-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [410 to 400]
    ##########################
    if x>=2.3 and x<3.5 and y<=4 and y>3.5: 
	    if x>float((3.5-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.5-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.45 and y>3 and y<=3.5: 
	    if x>float((3.45-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.45-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.4 and x<3.4 and y>2.5 and y<=3: 
	    if x>float((3.4-2.4)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.4)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.5 and x<3.4 and y>2 and y<=2.5: 
	    if  x>float((3.4-2.5)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.5)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.55 and x<3.4 and y>1.5 and y<=2:
	    if x>float((3.4-2.55)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.55)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.5 and x<3.4 and y>1 and y<=1.5: 
	    if x>float((3.4-2.5)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.5)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.45 and x<3.4 and y>0.5 and y<=1: 
	    if x>float((3.4-2.45)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.45)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.4 and x<3.4 and y>0 and y<=0.5: 
	    if x>float((3.4-2.4)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.4)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.4 and y>-0.5 and y<=0: 
	    if x>float((3.4-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.4 and y>-1 and y<=-0.5: 
	    if x>float((3.4-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.35 and y>-1.5 and y<=-1: 
	    if x>float((3.35-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.35-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.35 and y>-2 and y<=-1.5: 
	    if x>float((3.35-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.35-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.3 and y>-2.5 and y<=-2: 
	    if x>float((3.3-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.3-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.25 and y>-3 and y<=-2.5: 
	    if x>float((3.25-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.25-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.25 and x<3.2 and y>-3.5 and y<=-3: 
	    if x>float((3.2-2.25)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.2-2.25)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.2 and x<3.15 and y>=-4 and y<=-3.5: 
	    if x>float((3.15-2.2)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.15-2.2)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.2 and x<3.15 and y==-4: 
	    if x>float((3.15-2.2)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.15-2.2)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [400 to 390]
    ##########################
    if x>=3.5 and x<4 and y<=4 and y>3.5: 
	    if x>float((4-3.5)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.5)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.45 and x<4 and y>3 and y<=3.5: 
	    if x>float((4-3.45)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.45)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>2.5 and y<=3: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>2 and y<=2.5: 
	    if  x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>1.5 and y<=2:
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>1 and y<=1.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>0.5 and y<=1: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>0 and y<=0.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>-0.5 and y<=0: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>-1 and y<=-0.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.35 and x<4 and y>-1.5 and y<=-1: 
	    if x>float((4-3.35)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.35)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.35 and x<4 and y>-2 and y<=-1.5: 
	    if x>float((4-3.35)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.35)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.3 and x<4 and y>-2.5 and y<=-2: 
	    if x>float((4-3.3)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.3)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.25 and x<4 and y>-3 and y<=-2.5: 
	    if x>float((4-3.25)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.25)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.2 and x<4 and y>-3.5 and y<=-3: 
	    if x>float((4-3.2)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.2)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.15 and x<4 and y>=-4 and y<=-3.5: 
	    if x>float((4-3.15)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.15)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.15 and x<4 and y==-4: 
	    if x>float((4-3.15)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.15)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################
    #Raman range [390]
    ##########################
    if x==4 and y>=-4 and y<=4:
	    B2g=390; # at the right boundary
	    print 'B2g peak position: ',B2g,' cm-1'
    
    
    ##############################################################################
    ##############################################################################
    ##############################       Ag2      ################################	
    ##############################################################################	
    ##############################################################################
    
    ##########################
    #Raman range [476]
    ##########################
    if x==-4 and y>=-4 and y<=4:
	    Ag2=476; # at the left boundary
	    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    ##########################
    #Raman range [476 to 470]
    ##########################	
    
    if x>-4 and x<=-3 and y<=4 and y>3.5: 
	    if x>float((-4-3)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.05 and y>3 and y<=3.5:
	    if x>float((-4-3.05)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.05)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.1 and y>2.5 and y<=3: 
	    if x>float((-4-3.1)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.1)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.15 and y>2 and y<=2.5: 
	    if  x>float((-4-3.15)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.15)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.2 and y>1.5 and y<=2: 
	    if x>float((-4-3.2)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.2)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.3 and y>1 and y<=1.5: 
	    if x>float((-4-3.3)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.3)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>0.5 and y<=1: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.45 and y>0 and y<=0.5: 
	    if x>float((-4-3.45)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.45)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-0.5 and y<=0: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-1 and y<=-0.5: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-1.5 and y<=-1: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.55 and y>-2 and y<=-1.5: 
	    if x>float((-4-3.55)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.55)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-2.5 and y<=-2: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.45 and y>-3 and y<=-2.5: 
	    if x>float((-4-3.45)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.45)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>-3.5 and y<=-3: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>=-4 and y<=-3.5: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y==-4 : 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [470 to 465]
    ##########################	
    if x>-3 and x<=-1.95 and y<=4 and y>3.5: 
	    if x>float((-1.95-3)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.95-3)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.05 and x<=-2 and y>3 and y<=3.5:
	    if x>float((-2-3.05)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2-3.05)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.1 and x<=-2.1 and y>2.5 and y<=3: 
	    if x>float((-2.1-3.1)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.1-3.1)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.15 and x<=-2.05 and y>2 and y<=2.5: 
	    if  x>float((-2.05-3.15)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.05-3.15)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.2 and x<=-2.2 and y>1.5 and y<=2: 
	    if x>float((-2.2-3.2)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.2-3.2)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.3 and x<=-2.3 and y>1 and y<=1.5: 
	    if x>float((-2.3-3.3)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.3-3.3)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.45 and y>0.5 and y<=1: 
	    if x>float((-2.45-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.45 and x<=-2.55 and y>0 and y<=0.5: 
	    if x>float((-2.55-3.45)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55-3.45)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.6 and y>-0.5 and y<=0: 
	    if x>float((-2.6-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.6-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.55 and y>-1 and y<=-0.5: 
	    if x>float((-2.55-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.45 and y>-1.5 and y<=-1: 
	    if x>float((-2.45-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.55 and x<=-2.4 and y>-2 and y<=-1.5: 
	    if x>float((-2.4-3.55)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.4-3.55)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.45 and y>-2.5 and y<=-2:
	    if x>float((-2.45-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.45 and x<=-2.5 and y>-3 and y<=-2.5: 
	    if x>float((-2.5-3.45)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.5-3.45)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.7 and y>-3.5 and y<=-3: 
	    if x>float((-2.7-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.7-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.8 and y>=-4 and y<=-3.5: 
	    if x>float((-2.8-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.8-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.9 and y==-4 : 
	    if x>float((-2.9-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.9-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [465 to 455]
    ##########################	
    if x>-1.95 and x<=0.5 and y<=4 and y>3.5: 
	    if x>float((0.5-1.95)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.5-1.95)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2 and x<=0.5 and y>3 and y<=3.5:
	    if x>float((0.5-2)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.5-2)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.1 and x<=0.4 and y>2.5 and y<=3: 
	    if x>float((0.4-2.1)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.4-2.1)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.05 and x<=0.35 and y>2 and y<=2.5: 
	    if  x>float((0.35-2.05)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.35-2.05)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.2 and x<=0.3 and y>1.5 and y<=2: 
	    if x>float((0.3-2.2)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.2)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.3 and x<=0.3 and y>1 and y<=1.5: 
	    if x>float((0.3-2.3)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.3)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<0.3 and y>0.5 and y<=1: 
	    if x>float((0.3-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.55 and x<=0.25 and y>=0 and y<=0.5:
	    if x>float((0.25-2.55)/2):
		    if x==0 and y==0:
				    Ag2=456
				    print 'Ag2 peak position: ',Ag2,' cm-1'	
		    elif x!=0 and y!=0:
			    Ag2=float((465+455)/2)
			    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.25-2.55)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.6 and x<=0.2 and y>-0.5 and y<=0: 
	    if x>float((0.2-2.6)/2):
		    if x==0 and y==0:
			    Ag2=456
			    print 'Ag2 peak position: ',Ag2,' cm-1'	
		    elif x!=0 and y!=0:
			    Ag2=float((465+455)/2)
			    print 'Ag2 peak position: ',Ag2,' cm-1'		
	    elif x<=float((0.2-2.6)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.55 and x<=0 and y>-1 and y<=-0.5: 
	    if x>float((-2.55)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<=-0.3 and y>-1.5 and y<=-1: 
	    if x>float((-0.3-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.3-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.4 and x<=-0.5 and y>-2 and y<=-1.5: 
	    if x>float((-0.5-2.4)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.5-2.4)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<=-0.7 and y>-2.5 and y<=-2: 
	    if x>float((-0.7-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.7-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.5 and x<=-0.9 and y>-3 and y<=-2.5: 
	    if x>float((-0.9-2.5)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.9-2.5)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.7 and x<=-1.1 and y>-3.5 and y<=-3: 
	    if x>float((-1.1-2.7)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.1-2.7)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.8 and x<=-1.35 and y>=-4 and y<=-3.5: 
	    if x>float((-1.35-2.8)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.35-2.8)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.9 and x<=-1.5 and y==-4 : 
	    if x>float((-1.5-2.9)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.5-2.9)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [455 to 450]
    ##########################	
    if x>0.5 and x<=1.55 and y<=4 and y>3.5: 
	    if x>float((1.55+0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.55+0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.5 and x<=1.7 and y>3 and y<=3.5:
	    if x>float((1.7+0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.7+0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.4 and x<=2.05 and y>2.5 and y<=3: 
	    if x>float((2.05+0.4)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.05+0.4)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.35 and x<=2.3 and y>2 and y<=2.5: 
	    if  x>float((2.3+0.35)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.3+0.35)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.3 and x<=2.35 and y>1.5 and y<=2: 
	    if x>float((2.35+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.35+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>=0.3 and x<=2.2 and y>1 and y<=1.5: 
	    if x>float((2.2+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.2+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>=0.3 and x<=1.85 and y>0.5 and y<=1: 
	    if x>float((1.85+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.85+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.25 and x<=1.5 and y>0 and y<=0.5: 
	    if x>float((1.5+0.25)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.5+0.25)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.2 and x<=1.2 and y>-0.5 and y<=0: 
	    if x>float((1.2+0.2)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2+0.2)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0 and x<=1 and y>-1 and y<=-0.5: 
	    if x>float((1)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.3 and x<=0.8 and y>-1.5 and y<=-1: 
	    if x>float((0.8-0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.8-0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.5 and x<=0.5 and y>-2 and y<=-1.5: 
	    if x>0:
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<0:
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.7 and x<=0.15 and y>-2.5 and y<=-2: 
	    if x>float((-0.7+0.15)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.7+0.15)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.9 and x<=-0.05 and y>-3 and y<=-2.5: 
	    if x>float((-0.9-0.05)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.9-0.05)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.1 and x<=-0.3 and y>-3.5 and y<=-3: 
	    if x>float((-1.1-0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.1-0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.35 and x<=-0.5 and y>=-4 and y<=-3.5: 
	    if x>float((-1.35-0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.35-0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.5 and x<=-0.7 and y==-4 : 
	    if x>float((-1.5-0.7)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.5-0.7)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [450 to 445]
    ##########################	
    if x>1.55 and x<=4 and y<=4 and y>3.5: 
	    if x>float((1.55+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.55+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.7 and x<=4 and y>3 and y<=3.5:
	    if x>float((1.7+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.7+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.05 and x<=4 and y>2.85 and y<=3: 
	    if x>float((2.05+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.05+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.3 and x<=3.55 and y>2 and y<=2.85: 
	    if  x>float((2.3+3.55)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.3+2.55)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.35 and x<=3.55 and y>1.5 and y<=2: 
	    if x>float((2.35+3.55)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.35+3.55)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.2 and x<=3.34 and y>1 and y<=1.5: 
	    if x>float((2.2+3.34)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.2+3.34)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.85 and x<=3.05 and y>0.5 and y<=1: 
	    if x>float((1.85+3.05)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.85+3.05)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.5 and x<=2.8 and y>0 and y<=0.5: 
	    if x>float((1.5+2.8)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.5+2.8)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.2 and x<=2.4 and y>-0.5 and y<=0: 
	    if x>float((1.2+2.4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2+2.4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1 and x<=2.15 and y>-1 and y<=-0.5: 
	    if x>float((2.15+1)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1+2.15)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.8 and x<=2 and y>-1.5 and y<=-1: 
	    if x>float((0.8+2)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.8+2)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.5 and x<=1.8 and y>-2 and y<=-1.5: 
	    if x>float((0.5+1.8)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((0.5+1.8)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.15 and x<=1.45 and y>-2.5 and y<=-2: 
	    if x>float((1.45+0.15)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.45+0.15)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.05 and x<=1.2 and y>-3 and y<=-2.5: 
	    if x>float((1.2-0.05)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2-0.05)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.3 and x<=0.85 and y>-3.5 and y<=-3: 
	    if x>float((0.85-0.3)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.85-0.3)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.5 and x<=0.6 and y>=-4 and y<=-3.5: 
	    if x>float((0.6-0.5)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.6-0.5)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.7 and x<=0.3 and y==-4 : 
	    if x>float((0.3-0.7)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-0.7)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
		    
    ##########################
    #Raman range [445 to 440]
    ##########################	
    if x==4 and y==2.85: 
	    Ag2=445
	    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x>3.8 and x<=4 and y<2.85 and y>2.5: 
	    if x>float((3.8+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.8+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.55 and x<4 and y>2 and y<=2.5:
	    if x>float((3.55+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.55+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.34 and x<4 and y>1.5 and y<=2: 
	    if x>float((3.34+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.34+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.05 and x<4 and y>1 and y<=1.5: 
	    if  x>float((3.05+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.05+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.8 and x<4 and y>0.5 and y<=1: 
	    if x>float((2.8+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.8+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.4 and x<4 and y>0 and y<=0.5: 
	    if x>float((2.4+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.4+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x>2.15 and x<4 and y>-0.5 and y<=0: 
	    if x>float((2.15+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.15+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x==4 and y==-0.5:
	    Ag2=440
	    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2 and x<3.8 and y>-1 and y<-0.5: 
	    if x>float((2+3.8)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2+3.8)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.8 and x<3.5 and y>-1.5 and y<=-1: 
	    if x>float((1.8+3.5)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.8+3.5)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.45 and x<3.2 and y>-2 and y<=-1.5: 
	    if x>float((3.2+1.45)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.2+1.45)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.2 and x<2.9 and y>-2.5 and y<=-2: 
	    if x>float((2.9+1.2)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.9+1.2)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.85 and x<2.6 and y>-3 and y<=-2.5: 
	    if x>float((2.6+0.85)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((2.6+0.85)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.6 and x<2.2 and y>-3.5 and y<=-3: 
	    if x>float((0.6+2.2)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.6+2.2)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.3 and x<1.9 and y>=-4 and y<=-3.5: 
	    if x>float((1.9+0.3)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.9+0.3)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [440 to 435]
    ##########################	
    
    if x>3.8 and x<4 and y>-1 and y<-0.5: 
	    if x>float((4+3.8)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+3.8)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.5 and x<4 and y>-1.5 and y<=-1: 
	    if x>float((4+3.5)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+3.5)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.2 and x<4 and y>-2 and y<=-1.5: 
	    if x>float((3.2+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.2+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.9 and x<4 and y>-2.5 and y<=-2: 
	    if x>float((2.9+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.9+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.6 and x<4 and y>-3 and y<=-2.5: 
	    if x>float((2.6+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((2.6+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.2 and x<4 and y>-3.5 and y<=-3: 
	    if x>float((4+2.2)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+2.2)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.9 and x<4 and y>=-4 and y<=-3.5: 
	    if x>float((1.9+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.9+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x==4 and y==-4: 
	    Ag2=435
	    print 'Ag2 peak position: ',Ag2,' cm-1'
	    
    m=[]
    r=[]
    n=0
    while n<2001:
	l=300+0.1*n
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
    deltaEgap_3=round(deltaEgap_3,3)
    plt.text(400,5.8,deltaEgap_3,color='blue',fontsize=10)
    plt.text(370,5.8,'delta_Egap2:',color='blue',fontsize=10)
    plt.text(420,5.8,'eV:',color='blue',fontsize=10)    
    plt.text(Ag1-2,5,float(Ag1),color='blue',fontsize=10)
    plt.text(B2g-2,3.5,float(B2g),color='blue',fontsize=10)
    plt.text(Ag2-2,5.4,float(Ag2),color='blue',fontsize=10)
    plt.show()
    print '                                            '

#Case 4: for a general in-plain strain 
#global Ag1,B2g,x,y,Ag2
elif m!=l and l!=0:#and n==0:# and k==0:
    global deltaEgap_4,Ag1,Ag2,B2g
    x=m*100
    y=l*100
    print 'a general in-plain strain!!!!'
    if m==0:
	print 'And it is also in-plain uniaxial strain!!!!'
    print '                                            '
    phai()
    deltaEgap_case4()
    dd=round(deltaEgap_4,3)
    print 'delta_Egap4:',dd,'eV'
    ##############################################################################
    ##############################################################################
    ##############################       Ag1      ################################	
    ##############################################################################	
    ##############################################################################
    #############################
    #Raman range [346] boundary
    #############################	
    if x==4 and y==4:
	    Ag1=346
	    print 'Ag1 peak position: ',Ag1,' cm-1'
			    
    ##########################
    #Raman range [350 to 346] 
    ##########################	
    if x>=3.5 and x<4 and y<4 and y>2.1: 
	    if y>float((4+2.1)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.1)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<=4 and y>2.8 and x>=3 and x<3.5: 
	    if y>float((4+2.8)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.8)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<=4 and y>3.4 and x>=2.5 and x<3: 
	    if y>float((3.4+4)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+4)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    if y<=4 and y>3.8 and x>=2.5 and x<3: 
	    if y>float((4+3.8)/2):
		    Ag1=float((350+346)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.8)/2):
		    Ag1=350
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
		    
    ##########################
    #Raman range [354 to 350] 
    ##########################	
    if y<=2.1 and y>=0.4 and x>=3.5 and x<4: 
	    if y>float((0.4+2.1)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.4+2.1)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<=2.8 and y>=1.1 and x>=3 and x<3.5: 
	    if y>float((1.8+1.1)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8+1.1)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<=3.4 and y>=1.8 and x>=2.5 and x<3: 
	    if y>float((2.4+1.8)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4+1.8)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    if y<=3.8 and y>=2.4 and x>=2 and x<2.5: 
	    if y>float((2.8+2.4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+2.4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=2.8 and x>=0.5 and x<2: 
	    if y>float((2.8+4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<=4 and y>=3.4 and x>=0 and x<0.5: 
	    if y>float((3.4+4)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+4)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=3.6 and x>=-0.5 and x<0: 
	    if y>float((4+3.6)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((4+3.6)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'	
    
    if y<=4 and y>=3.9 and x>=-0.7 and x<-0.5: 
	    if y>float((4+3.9)/2):
		    Ag1=float((350+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((4+3.9)/2):
		    Ag1=354
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y==4 and x==-0.7:
	    Ag1=354
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
	    
    ##########################
    #Raman range [358 to 354] 
    ##########################
    if y<0.4 and y>=-1.2 and x>=3.5 and x<4: 
	    if y>float((0.4-1.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.4-2.1)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    
    if y<1.1 and y>=-0.6 and x>=3 and x<3.5: 
	    if y>float((1.1-0.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.1-0.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.8 and y>=-0.1 and x>=2.5 and x<3: 
	    if y>float((1.8-0.1)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8-0.1)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.4 and y>=0.6 and x>=2 and x<2.5: 
	    if y>float((2.4+0.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4+0.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.8 and y>=1.4 and x>=0.5 and x<2: 
	    if y>float((2.8+1.4)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.8+1.4)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.4 and y>=2.2 and x>=0 and x<0.5: 
	    if y>float((3.4+2.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.4+2.2)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.6 and y>=2.3 and x>=-0.5 and x<0: 
	    if y>float((3.6+2.3)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.6+2.3)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.6 and x>=-0.7 and x<-0.5: 
	    if y>float((4+2.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.9 and x>=-1 and x<-0.7: 
	    if y>float((4+2.6)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.6)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'		
		    
    if y<4 and y>=2.9 and x>=-1.5 and x<-1: 
	    if y>float((4+2.9)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.9)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.2 and x>=-2 and x<-1.5: 
	    if y>float((4+3.2)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.2)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.5 and x>=-2.5 and x<-2: 
	    if y>float((4+3.5)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.5)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<4 and y>=3.7 and x>=-3.3 and x<-2.5: 
	    if y>float((4+3.7)/2):
		    Ag1=float((358+354)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+3.7)/2):
		    Ag1=358
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if x==-3.3 and y==4:
	    Ag1=358
	    print 'Ag1 peak position: ',Ag1,' cm-1'		
    ##########################
    #Raman range [362 to 358] 
    ##########################
    if y<-1.2 and y>=-3.2 and x>=3.5 and x<4: 
	    if y>float((-3.2-1.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y>float((-3.2-1.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.6 and y>=-2.2 and x>=3 and x<3.5: 
	    if y>float((-0.6-2.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.6-2.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.1 and y>=-1.6 and x>=2.5 and x<3: 
	    if y>float((-0.1-1.6)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.1-1.6)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.6 and y>=-1 and x>=2 and x<2.5: 
	    if y>float((0.6-1)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.6-1)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.4 and y>=-0.5 and x>=1.5 and x<2: 
	    if y>float((1.4-0.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.4-0.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.9 and y>=0.2 and x>=1 and x<1.5: 
	    if y>float((1.9+0.2)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.9+0.2)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.05 and y>=0.8 and x>=0.5 and x<1: 
	    if y>float((2.05+0.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.05+0.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.2 and y>=0.8 and x>=0  and x<0.5: 
	    if y>float((2.2+0.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.2+0.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.3 and y>=1.3 and x>=-0.5  and x<0: 
	    if y>float((2.3+1.3)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.3+1.3)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.6 and y>=1.5 and x>=-1  and x<-0.5: 
	    if y>float((2.6+1.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.6+1.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.9 and y>=1.7 and x>=-1.5  and x<-1: 
	    if y>float((2.9+1.7)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.9+1.7)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.2 and y>=1.8 and x>=-2  and x<-1.5: 
	    if y>float((3.2+1.8)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.2+1.8)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.5 and y>=2.1 and x>=-2.5  and x<-2: 
	    if y>float((3.5+2.1)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.5+2.1)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<3.7 and y>=2.3 and x>=-3.3  and x<-2.5: 
	    if y>float((3.7+2.3)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((3.7+2.3)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.45 and x>=-3.5  and x<-3.3: 
	    if y>float((4+2.45)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.45)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<4 and y>=2.5 and x>=-4  and x<-3.5: 
	    if y>float((4+2.5)/2):
		    Ag1=float((358+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((4+2.5)/2):
		    Ag1=362
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    ##########################
    #Raman range [366 to 362] 
    ##########################	
    if x==-4 and y==4:
	    Ag1=360
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
    if x==4 and y==-4:
	    Ag1=364
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
	    
    if y<-3.2 and y>=-4 and x>=3.6  and x<4: 
	    if y>float((-4-3.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.2 and y>=-3.8 and x>=3.5  and x<3.6: 
	    if y>float((-3.8-2.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.8-2.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.2 and y>=-3.8 and x>=3  and x<3.5: 
	    if y>float((-3.8-2.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.8-2.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.6 and y>=-3.1 and x>=2.5  and x<3: 
	    if y>float((-1.6-3.1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-1.6-3.1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1 and y>=-2.4 and x>=2  and x<2.5: 
	    if y>float((-2.4-1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.4-1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.5 and y>=-1.9 and x>=1.5  and x<2: 
	    if y>float((-0.5-1.9)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.5-1.9)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<0.2 and y>=-1.4 and x>=1  and x<1.5: 
	    if y>float((0.2-1.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.2-1.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.8 and y>=-0.8 and x>=0.5  and x<1: 
	    if y>float((0.8-0.8)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.8-0.8)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.2 and y>=0 and x>=0  and x<0.5: 
	    if y>float((1.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.2)/2):
		    if x==0 and y==0:
			    Ag1=368
			    print 'Ag1 peak position: ',Ag1,' cm-1'
		    elif x!=0 and y!=0:
			    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<1.2 and y>=0 and x>=0  and x<0.5: 
	    if y>float((1.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.2)/2):
		    if x==0 and y==0:
			    Ag1=368
			    print 'Ag1 peak position: ',Ag1,' cm-1'
		    elif x!=0 and y!=0:
			    Ag1=366
			    print 'Ag1 peak position: ',Ag1,' cm-1'    		    
		    
		    
    if y<1.3 and y>=0.4 and x>=-0.5  and x<0: 
	    if y>float((1.3-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.3-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.5 and y>=0.5 and x>=-1 and x<-0.5: 
	    if y>float((1.5-0.5)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.5-0.5)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.7 and y>=0.5 and x>=-1.5 and x<-1: 
	    if y>float((1.7-0.5)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.7-0.5)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<1.8 and y>=0.4 and x>=-2 and x<-1.5: 
	    if y>float((1.8-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((1.8-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.1 and y>=0.2 and x>=-2.5 and x<-2: 
	    if y>float((2.1-0.2)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.1-0.2)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.3 and y>=0.1 and x>=-3 and x<-2.5: 
	    if y>float((2.3-0.1)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.3-0.1)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.35 and y>=-0.05 and x>=-3.5 and x<-3: 
	    if y>float((2.4-0.05)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4-0.05)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<2.4 and y>=-0.4 and x>=-4 and x<-3.5: 
	    if y>float((2.4-0.4)/2):
		    Ag1=float((366+362)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((2.4-0.4)/2):
		    Ag1=366
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    ##########################
    #Raman range [370 to 366] 
    ##########################
    if y<-3.1 and y>=-4 and x>=3 and x<3.6: 
	    if y>float((-4-3.1)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.1)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.4 and y>=-4 and x>=2.4 and x<3: 
	    if y>float((-2.4-4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.4-4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-1.9 and x>=2 and x<2.4: 
	    if y>float((-3.5-1.9)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-1.9)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-1.9 and x>=1.5 and x<2: 
	    if y>float((-3.5-1.9)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-1.9)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.4 and y>=-3.1 and x>=1.0 and x<1.5: 
	    if y>float((-3.1-1.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.1-1.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.8 and y>=-2.8 and x>=0.5 and x<1: 
	    if y>float((-2.8-0.8)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.8-0.8)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0 and y>=-2.5 and x>=0 and x<0.5: 
	    if y>float((-2.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.4 and y>=-2.1 and x>=-0.5 and x<=0: 
	    if y>float((-2.1-0.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-2.1-0.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.5 and y>=-1.1 and x>=-1 and x<-0.5: 
	    if y>float((-1.1-0.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-1.1-0.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.5 and y>=-0.8 and x>=-1.5 and x<-1: 
	    if y>float((-0.8-0.5)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.8-0.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<0.4 and y>=-0.8 and x>=-2 and x<-1.5: 
	    if y>float((-0.8-0.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.8-0.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.2 and y>=-1 and x>=-2.5 and x<-2: 
	    if y>float((0.2-1)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.2-1)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<0.1 and y>=-1.2 and x>=-3 and x<-2.5: 
	    if y>float((0.1-1.2)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.1-1.2)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.05 and y>=-2 and x>=-3.5 and x<-3: 
	    if y>float((0.1-1.2)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((0.1-1.2)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-0.4 and y>=-2.4 and x>-4 and x<-3.5: 
	    if y>float((-0.4-2.4)/2):
		    Ag1=float((370+366)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-0.4-2.4)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if x==-4 and y==-1.2:
	    Ag1=366
	    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if x==-4 and y==-2.6:
	    Ag1=370
	    print 'Ag1 peak position: ',Ag1,' cm-1'	
		    
    ##########################
    #Raman range [374 to 370] 
    ##########################
    if y<-3.5 and y>=-4 and x>=2 and x<2.4: 
	    if y>float((-4-3.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.5)/2):
		    Ag1=371
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    if y<-3.5 and y>=-4 and x>=0.5 and x<2: 
	    if y>float((-4-3.5)/2):
		    Ag1=370
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-3.5)/2):
		    Ag1=371
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.5 and y>=-4 and x>=-0.5 and x<0.5: 
	    if y>float((-4-2.5)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-2.5)/2):
		    Ag1=372
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1.1 and y>=-4 and x>=-2 and x<-0.5: 
	    if y>float((-4-1.1)/2):
		    Ag1=float((371+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-1.1)/2):
		    Ag1=373
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-1 and y>=-4 and x>=-2.7 and x<-2: 
	    if y>float((-4-1)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-4-1)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2 and y>=-3.7 and x>=-3 and x<-2.7: 
	    if y>float((-3.7-2)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.7-2)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.4 and y>=-3.4 and x>=-3.5 and x<-3: 
	    if y>float((-3.4-2.4)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.4-2.4)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-2.6 and y>=-3.3 and x>=-4 and x<-3.5: 
	    if y>float((-3.3-2.6)/2):
		    Ag1=float((370+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.3-2.6)/2):
		    Ag1=374
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    #############################
    #Raman range [378] boundary
    #############################		
    if y<-3.7 and y>=-4 and x>=-3 and x<-2.7: 
	    if y>float((-3.7-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.7-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.5 and y>=-4 and x>=-3.5 and x<-3: 
	    if y>float((-3.5-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.5-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
		    
    if y<-3.4 and y>=-4 and x>=-4 and x<-3.5: 
	    if y>float((-3.4-4)/2):
		    Ag1=float((378+374)/2)
		    print 'Ag1 peak position: ',Ag1,' cm-1'
	    elif y<=float((-3.4-4)/2):
		    Ag1=378
		    print 'Ag1 peak position: ',Ag1,' cm-1'
    
    
    
    
    ##############################################################################
    ##############################################################################
    ##############################       B2g      ################################	
    ##############################################################################	
    ##############################################################################
    
    
    
    ##########################
    #Raman range [465]
    ##########################
    if x==-4 and y>=-4 and y<=4:
	    B2g=465; # at the left boundary
	    print 'B2g peak position: ',B2g,' cm-1'
    
    
    ##########################
    #Raman range [465 to 456]
    ##########################	
    if x>-4 and x<-3.5 and y<=4 and y>3.5: # I set the mesh for 0.25, -3.5
	    if x>-3.75:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.75:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.45 and y>3 and y<=3.5: # I set the mesh for 0.275, -3.45 
	    if x>-3.725:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.725:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.4 and y>2.5 and y<=3: # I set the mesh for 0.3, -3.4
	    if x>-3.7:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.7:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.35 and y>2 and y<=2.5: # I set the mesh for 0.325, -3.35
	    if  x>-3.675:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.675:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.3 and y>1.5 and y<=2: # I set the mesh for 0.3, -3.3
	    if x>-3.65:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.65:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.25 and y>1 and y<=1.5: # I set the mesh for 0.375, -3.25 
	    if x>-3.625:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.625:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.2 and y>0.5 and y<=1: # I set the mesh for 0.4,-3.2 
	    if x>-3.6:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.6:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.15 and y>0 and y<=0.5: # I set the mesh for 0.425,-3.15
	    if x>-3.575:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.575:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.1 and y>-0.5 and y<=0: # I set the mesh for 0.45, -3.1
	    if x>-3.55:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.55:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3.05 and y>-1 and y<=-0.5: # I set the mesh for 0.475, -3.05
	    if x>-3.525:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.525:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-3 and y>-1.5 and y<=-1: # I set the mesh for 0.5, -3
	    if x>-3.5:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.5:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.9 and y>-2 and y<=-1.5: # I set the mesh for 0.55, -2.9
	    if x>-3.45:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.45:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.8 and y>-2.5 and y<=-2: # I set the mesh for 0.6, -2.8
	    if x>-3.4:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.4:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.75 and y>-3 and y<=-2.5: # I set the mesh for 0.625, -2.75
	    if x>-3.375:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.375:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.8 and y>-3.5 and y<=-3: # I set the mesh for 0.6, -2.8
	    if x>-3.4:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.4:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.85 and y>=-4 and y<=-3.5: # I set the mesh for 0.575, -2.85
	    if x>-3.425:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.425:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>-4 and x<-2.9 and y==-4 : # I set the mesh for 0.55, -2.9
	    if x>-3.45:
		    B2g=float((465+456)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=-3.45:
		    B2g=465
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [456 to 447]
    ##########################	
    if x>=-3.5 and x<-2.2 and y<=4 and y>3.5: 
	    if x>float((-3.5-2.2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.5-2.2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.45 and x<-2.15 and y>3 and y<=3.5: 
	    if x>float((-3.45-2.15)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.45-2.15)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.4 and x<-2.1 and y>2.5 and y<=3: 
	    if x>float((-3.4-2.1)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.4-2.1)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.35 and x<-2.05 and y>2 and y<=2.5: 
	    if  x>float((-3.35-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.35-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.3 and x<-2.05 and y>1.5 and y<=2: 
	    if x>float((-3.3-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.3-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.25 and x<-2.05 and y>1 and y<=1.5: 
	    if x>float((-3.25-2.05)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.25-2.05)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.2 and x<-2 and y>0.5 and y<=1:
	    if x>float((-3.2-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.2-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.15 and x<-2 and y>0 and y<=0.5: 
	    if x>float((-3.15-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<float((-3.15-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.1 and x<-2 and y>-0.5 and y<=0: 
	    if x>float((-3.1-2)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.1-2)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3.05 and x<-1.9 and y>-1 and y<=-0.5: 
	    if x>float((-3.05-1.9)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.05-1.9)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-3 and x<-1.8 and y>-1.5 and y<=-1: 
	    if x>float((-3-1.8)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3-1.8)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.9 and x<-1.7 and y>-2 and y<=-1.5: 
	    if x>float((-2.9-1.7)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.9-1.7)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.8 and x<-1.65 and y>-2.5 and y<=-2: 
	    if x>float((-2.8-1.65)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.8-1.65)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.75 and x<-1.66 and y>-3 and y<=-2.5: 
	    if x>float((-2.75-1.66)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.75-1.66)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.8 and x<-1.7 and y>-3.5 and y<=-3: 
	    if x>float((-2.8-1.7)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.8-1.7)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.85 and x<-1.75 and y>-4 and y<=-3.5: # I set the mesh for 0.625, -2.85
	    if x>float((-2.85-1.75)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.85-1.75)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'
    
    if x>=-2.9 and x<-1.8 and y==-4: 
	    if x>float((-2.9-1.8)/2):
		    B2g=float((456+447)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-2.9-1.8)/2):
		    B2g=456
		    print 'B2g peak position: ',B2g,' cm-1'		
    ##########################		
    #Raman range [447 to 438]
    ##########################
    if x>=-2.2 and x<-1 and y<=4 and y>3.5: 
	    if x>float((-1-2.2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-1-2.2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.15 and x<-0.95 and y>3 and y<=3.5: 
	    if x>float((-0.95-2.15)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.15)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.1 and x<-0.95 and y>2.5 and y<=3: 
	    if x>float((-0.95-2.1)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.1)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.95 and y>2 and y<=2.5: 
	    if  x>float((-0.95-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.9 and y>1.5 and y<=2:
	    if x>float((-0.9-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.9-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2.05 and x<-0.85 and y>1 and y<=1.5: 
	    if x>float((-0.85-2.05)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.85-2.05)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.8 and y>0.5 and y<=1: 
	    if x>float((-0.8-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.8-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.75 and y>0 and y<=0.5: 
	    if x>float((-0.75-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-3.15-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-2 and x<-0.7 and y>-0.5 and y<=0: 
	    if x>float((-0.7-2)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-2)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.9 and x<-0.6 and y>-1 and y<=-0.5: 
	    if x>float((-0.6-1.9)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.9)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.8 and x<-0.55 and y>-1.5 and y<=-1: 
	    if x>float((-0.55-1.8)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.55-1.8)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.7 and x<-0.6 and y>-2 and y<=-1.5: 
	    if x>float((-0.6-1.7)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.7)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.65 and x<-0.6 and y>-2.5 and y<=-2: 
	    if x>float((-0.6-1.65)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.65)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.66 and x<-0.6 and y>-3 and y<=-2.5: 
	    if x>float((-0.6-1.66)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-1.66)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.7 and x<-0.65 and y>-3.5 and y<=-3: 
	    if x>float((-0.65-1.7)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.65-1.7)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.75 and x<-0.7 and y>=-4 and y<=-3.5: 
	    if x>float((-0.7-1.75)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-1.75)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-1.8 and x<-0.75 and y==-4: 
	    if x>float((-0.75-1.8)/2):
		    B2g=float((447+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-1.8)/2):
		    B2g=447
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [438 to 428]
    ##########################
    if x>=-1 and x<0.35 and y<=4 and y>3.5: 
	    if x>float((-1-0.35)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-1-0.35)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>3 and y<=3.5: 
	    if x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>2.5 and y<=3: 
	    if x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.95 and x<0.4 and y>2 and y<=2.5: 
	    if  x>float((-0.95-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.95-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.9 and x<0.45 and y>1.5 and y<=2:
	    if x>float((-0.9-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.9-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.85 and x<0.5 and y>1 and y<=1.5: 
	    if x>float((-0.85-0.5)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.85-0.5)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.8 and x<0.55 and y>0.5 and y<=1: 
	    if x>float((-0.8-0.55)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.8-0.55)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.75 and x<0.6 and y>0 and y<=0.5: 
	    if x>float((-0.75-0.6)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-0.6)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.7 and x<0.6 and y>-0.5 and y<=0: 
	    if x>float((-0.7-0.6)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-0.6)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.55 and y>-1 and y<=-0.5: 
	    if x>float((-0.6-0.55)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.55)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.55 and x<0.5 and y>-1.5 and y<=-1: 
	    if x>float((-0.55-0.5)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.55-0.5)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.45 and y>-2 and y<=-1.5: 
	    if x>float((-0.6-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.4 and y>-2.5 and y<=-2: 
	    if x>float((-0.6-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.6 and x<0.4 and y>-3 and y<=-2.5: 
	    if x>float((-0.6-0.4)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.6-0.4)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.65 and x<0.45 and y>-3.5 and y<=-3: 
	    if x>float((-0.65-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.65-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.7 and x<0.45 and y>=-4 and y<=-3.5: 
	    if x>float((-0.7-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.7-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=-0.75 and x<0.45 and y==-4: 
	    if x>float((-0.75-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((-0.75-0.45)/2):
		    B2g=438
		    print 'B2g peak position: ',B2g,' cm-1'
    
		    
    ##########################		
    #Raman range [428 to 419]
    ##########################
    if x>=0.35 and x<1.3 and y<=4 and y>3.5: 
	    if x>float((1.3-0.35)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.35)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.35 and y>3 and y<=3.5: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.4 and y>2.5 and y<=3: 
	    if x>float((1.4-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.5 and y>2 and y<=2.5: 
	    if  x>float((1.4-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.6 and y>1.5 and y<=2:
	    if x>float((1.6-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.6-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.5 and x<1.55 and y>1 and y<=1.5: 
	    if x>float((1.55-0.5)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.55-0.5)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.55 and x<1.5 and y>0.5 and y<=1: 
	    if x>float((1.5-0.55)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.5-0.55)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.6 and x<1.5 and y>0 and y<=0.5: 
	    if x>float((1.5-0.6)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.5-0.6)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.6 and x<1.45 and y>-0.5 and y<=0: 
	    if x>float((1.45-0.6)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.45-0.6)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.55 and x<1.45 and y>-1 and y<=-0.5: 
	    if x>float((1.45-0.55)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.45-0.55)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.5 and x<1.4 and y>-1.5 and y<=-1: 
	    if x>float((1.4-0.5)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.5)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.4 and y>-2 and y<=-1.5: 
	    if x>float((1.4-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.4-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.35 and y>-2.5 and y<=-2: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.4 and x<1.3 and y>-3 and y<=-2.5: 
	    if x>float((1.35-0.4)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.35-0.4)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y>-3.5 and y<=-3: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y>=-4 and y<=-3.5: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=0.45 and x<1.3 and y==-4: 
	    if x>float((1.3-0.45)/2):
		    B2g=float((428+438)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((1.3-0.45)/2):
		    B2g=428
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [419 to 410]
    ##########################
    if x>=1.3 and x<2.3 and y<=4 and y>3.5: 
	    if x>float((2.3-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.35 and x<2.35 and y>3 and y<=3.5: 
	    if x>float((2.35-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.4 and y>2.5 and y<=3: 
	    if x>float((2.4-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.4-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.5 and y>2 and y<=2.5: 
	    if  x>float((2.5-1.5)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.5)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.6 and x<2.55 and y>1.5 and y<=2:
	    if x>float((2.55-1.6)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.55-1.6)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.55 and x<2.5 and y>1 and y<=1.5: 
	    if x>float((2.5-1.55)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.55)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.45 and y>0.5 and y<=1: 
	    if x>float((2.5-1.55)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.5-1.55)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.5 and x<2.4 and y>0 and y<=0.5: 
	    if x>float((2.4-1.5)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.4-1.5)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.45 and x<2.35 and y>-0.5 and y<=0: 
	    if x>float((2.35-1.45)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.45)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.45 and x<2.35 and y>-1 and y<=-0.5: 
	    if x>float((2.35-1.45)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.35-1.45)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.3 and y>-1.5 and y<=-1: 
	    if x>float((2.3-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.4 and x<2.3 and y>-2 and y<=-1.5: 
	    if x>float((2.3-1.4)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.4)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.35 and x<2.3 and y>-2.5 and y<=-2: 
	    if x>float((2.3-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.3 and y>-3 and y<=-2.5: 
	    if x>float((2.3-1.35)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.3-1.35)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.25 and y>-3.5 and y<=-3: 
	    if x>float((2.25-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.25-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.2 and y>=-4 and y<=-3.5: 
	    if x>float((2.2-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.2-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=1.3 and x<2.2 and y==-4: 
	    if x>float((2.2-1.3)/2):
		    B2g=float((410+419)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((2.2-1.3)/2):
		    B2g=419
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [410 to 400]
    ##########################
    if x>=2.3 and x<3.5 and y<=4 and y>3.5: 
	    if x>float((3.5-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.5-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.45 and y>3 and y<=3.5: 
	    if x>float((3.45-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.45-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.4 and x<3.4 and y>2.5 and y<=3: 
	    if x>float((3.4-2.4)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.4)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.5 and x<3.4 and y>2 and y<=2.5: 
	    if  x>float((3.4-2.5)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.5)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.55 and x<3.4 and y>1.5 and y<=2:
	    if x>float((3.4-2.55)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.55)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.5 and x<3.4 and y>1 and y<=1.5: 
	    if x>float((3.4-2.5)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.5)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.45 and x<3.4 and y>0.5 and y<=1: 
	    if x>float((3.4-2.45)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.45)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.4 and x<3.4 and y>0 and y<=0.5: 
	    if x>float((3.4-2.4)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.4)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.4 and y>-0.5 and y<=0: 
	    if x>float((3.4-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.35 and x<3.4 and y>-1 and y<=-0.5: 
	    if x>float((3.4-2.35)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.4-2.35)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.35 and y>-1.5 and y<=-1: 
	    if x>float((3.35-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.35-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.35 and y>-2 and y<=-1.5: 
	    if x>float((3.35-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.35-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.3 and y>-2.5 and y<=-2: 
	    if x>float((3.3-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.3-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.3 and x<3.25 and y>-3 and y<=-2.5: 
	    if x>float((3.25-2.3)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.25-2.3)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.25 and x<3.2 and y>-3.5 and y<=-3: 
	    if x>float((3.2-2.25)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.2-2.25)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.2 and x<3.15 and y>=-4 and y<=-3.5: 
	    if x>float((3.15-2.2)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.15-2.2)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=2.2 and x<3.15 and y==-4: 
	    if x>float((3.15-2.2)/2):
		    B2g=float((410+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((3.15-2.2)/2):
		    B2g=410
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################		
    #Raman range [400 to 390]
    ##########################
    if x>=3.5 and x<4 and y<=4 and y>3.5: 
	    if x>float((4-3.5)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.5)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.45 and x<4 and y>3 and y<=3.5: 
	    if x>float((4-3.45)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.45)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>2.5 and y<=3: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>2 and y<=2.5: 
	    if  x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>1.5 and y<=2:
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>1 and y<=1.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>0.5 and y<=1: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>0 and y<=0.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>-0.5 and y<=0: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.4 and x<4 and y>-1 and y<=-0.5: 
	    if x>float((4-3.4)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.4)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.35 and x<4 and y>-1.5 and y<=-1: 
	    if x>float((4-3.35)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.35)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.35 and x<4 and y>-2 and y<=-1.5: 
	    if x>float((4-3.35)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.35)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.3 and x<4 and y>-2.5 and y<=-2: 
	    if x>float((4-3.3)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.3)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.25 and x<4 and y>-3 and y<=-2.5: 
	    if x>float((4-3.25)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.25)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.2 and x<4 and y>-3.5 and y<=-3: 
	    if x>float((4-3.2)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.2)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.15 and x<4 and y>=-4 and y<=-3.5: 
	    if x>float((4-3.15)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.15)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    if x>=3.15 and x<4 and y==-4: 
	    if x>float((4-3.15)/2):
		    B2g=float((390+400)/2)
		    print 'B2g peak position: ',B2g,' cm-1'
	    elif x<=float((4-3.15)/2):
		    B2g=400
		    print 'B2g peak position: ',B2g,' cm-1'
		    
    ##########################
    #Raman range [390]
    ##########################
    if x==4 and y>=-4 and y<=4:
	    B2g=390; # at the right boundary
	    print 'B2g peak position: ',B2g,' cm-1'
    
    
    ##############################################################################
    ##############################################################################
    ##############################       Ag2      ################################	
    ##############################################################################	
    ##############################################################################
    
    ##########################
    #Raman range [476]
    ##########################
    if x==-4 and y>=-4 and y<=4:
	    Ag2=476; # at the left boundary
	    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    ##########################
    #Raman range [476 to 470]
    ##########################	
    
    if x>-4 and x<=-3 and y<=4 and y>3.5: 
	    if x>float((-4-3)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.05 and y>3 and y<=3.5:
	    if x>float((-4-3.05)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.05)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.1 and y>2.5 and y<=3: 
	    if x>float((-4-3.1)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.1)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.15 and y>2 and y<=2.5: 
	    if  x>float((-4-3.15)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.15)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.2 and y>1.5 and y<=2: 
	    if x>float((-4-3.2)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.2)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.3 and y>1 and y<=1.5: 
	    if x>float((-4-3.3)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.3)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>0.5 and y<=1: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.45 and y>0 and y<=0.5: 
	    if x>float((-4-3.45)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.45)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-0.5 and y<=0: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-1 and y<=-0.5: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-1.5 and y<=-1: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.55 and y>-2 and y<=-1.5: 
	    if x>float((-4-3.55)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.55)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y>-2.5 and y<=-2: 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.45 and y>-3 and y<=-2.5: 
	    if x>float((-4-3.45)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.45)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>-3.5 and y<=-3: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.4 and y>=-4 and y<=-3.5: 
	    if x>float((-4-3.4)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.4)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-4 and x<=-3.5 and y==-4 : 
	    if x>float((-4-3.5)/2):
		    Ag2=float((476+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-4-3.5)/2):
		    Ag2=476
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [470 to 465]
    ##########################	
    if x>-3 and x<=-1.95 and y<=4 and y>3.5: 
	    if x>float((-1.95-3)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.95-3)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.05 and x<=-2 and y>3 and y<=3.5:
	    if x>float((-2-3.05)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2-3.05)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.1 and x<=-2.1 and y>2.5 and y<=3: 
	    if x>float((-2.1-3.1)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.1-3.1)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.15 and x<=-2.05 and y>2 and y<=2.5: 
	    if  x>float((-2.05-3.15)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.05-3.15)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.2 and x<=-2.2 and y>1.5 and y<=2: 
	    if x>float((-2.2-3.2)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.2-3.2)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.3 and x<=-2.3 and y>1 and y<=1.5: 
	    if x>float((-2.3-3.3)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.3-3.3)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.45 and y>0.5 and y<=1: 
	    if x>float((-2.45-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.45 and x<=-2.55 and y>0 and y<=0.5: 
	    if x>float((-2.55-3.45)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55-3.45)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.6 and y>-0.5 and y<=0: 
	    if x>float((-2.6-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.6-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.55 and y>-1 and y<=-0.5: 
	    if x>float((-2.55-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.45 and y>-1.5 and y<=-1: 
	    if x>float((-2.45-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.55 and x<=-2.4 and y>-2 and y<=-1.5: 
	    if x>float((-2.4-3.55)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.4-3.55)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.45 and y>-2.5 and y<=-2:
	    if x>float((-2.45-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.45-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.45 and x<=-2.5 and y>-3 and y<=-2.5: 
	    if x>float((-2.5-3.45)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.5-3.45)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.7 and y>-3.5 and y<=-3: 
	    if x>float((-2.7-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.7-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.4 and x<=-2.8 and y>=-4 and y<=-3.5: 
	    if x>float((-2.8-3.4)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.8-3.4)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-3.5 and x<=-2.9 and y==-4 : 
	    if x>float((-2.9-3.5)/2):
		    Ag2=float((465+470)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.9-3.5)/2):
		    Ag2=470
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [465 to 455]
    ##########################	
    if x>-1.95 and x<=0.5 and y<=4 and y>3.5: 
	    if x>float((0.5-1.95)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.5-1.95)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2 and x<=0.5 and y>3 and y<=3.5:
	    if x>float((0.5-2)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.5-2)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.1 and x<=0.4 and y>2.5 and y<=3: 
	    if x>float((0.4-2.1)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.4-2.1)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.05 and x<=0.35 and y>2 and y<=2.5: 
	    if  x>float((0.35-2.05)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.35-2.05)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.2 and x<=0.3 and y>1.5 and y<=2: 
	    if x>float((0.3-2.2)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.2)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.3 and x<=0.3 and y>1 and y<=1.5: 
	    if x>float((0.3-2.3)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.3)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<0.3 and y>0.5 and y<=1: 
	    if x>float((0.3-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.55 and x<=0.25 and y>=0 and y<=0.5:
	    if x>float((0.25-2.55)/2):
		    if x==0 and y==0:
				    Ag2=456
				    print 'Ag2 peak position: ',Ag2,' cm-1'	
		    elif x!=0 and y!=0:
			    Ag2=float((465+455)/2)
			    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.25-2.55)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.6 and x<=0.2 and y>-0.5 and y<=0: 
	    if x>float((0.2-2.6)/2):
		    if x==0 and y==0:
			    Ag2=456
			    print 'Ag2 peak position: ',Ag2,' cm-1'	
		    elif x!=0 and y!=0:
			    Ag2=float((465+455)/2)
			    print 'Ag2 peak position: ',Ag2,' cm-1'		
	    elif x<=float((0.2-2.6)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.55 and x<=0 and y>-1 and y<=-0.5: 
	    if x>float((-2.55)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-2.55)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<=-0.3 and y>-1.5 and y<=-1: 
	    if x>float((-0.3-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.3-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.4 and x<=-0.5 and y>-2 and y<=-1.5: 
	    if x>float((-0.5-2.4)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.5-2.4)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.45 and x<=-0.7 and y>-2.5 and y<=-2: 
	    if x>float((-0.7-2.45)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.7-2.45)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.5 and x<=-0.9 and y>-3 and y<=-2.5: 
	    if x>float((-0.9-2.5)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.9-2.5)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.7 and x<=-1.1 and y>-3.5 and y<=-3: 
	    if x>float((-1.1-2.7)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.1-2.7)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.8 and x<=-1.35 and y>=-4 and y<=-3.5: 
	    if x>float((-1.35-2.8)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.35-2.8)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-2.9 and x<=-1.5 and y==-4 : 
	    if x>float((-1.5-2.9)/2):
		    Ag2=float((465+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.5-2.9)/2):
		    Ag2=465
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [455 to 450]
    ##########################	
    if x>0.5 and x<=1.55 and y<=4 and y>3.5: 
	    if x>float((1.55+0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.55+0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.5 and x<=1.7 and y>3 and y<=3.5:
	    if x>float((1.7+0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.7+0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.4 and x<=2.05 and y>2.5 and y<=3: 
	    if x>float((2.05+0.4)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.05+0.4)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.35 and x<=2.3 and y>2 and y<=2.5: 
	    if  x>float((2.3+0.35)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.3+0.35)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.3 and x<=2.35 and y>1.5 and y<=2: 
	    if x>float((2.35+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.35+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>=0.3 and x<=2.2 and y>1 and y<=1.5: 
	    if x>float((2.2+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.2+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>=0.3 and x<=1.85 and y>0.5 and y<=1: 
	    if x>float((1.85+0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.85+0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.25 and x<=1.5 and y>0 and y<=0.5: 
	    if x>float((1.5+0.25)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.5+0.25)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.2 and x<=1.2 and y>-0.5 and y<=0: 
	    if x>float((1.2+0.2)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2+0.2)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0 and x<=1 and y>-1 and y<=-0.5: 
	    if x>float((1)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.3 and x<=0.8 and y>-1.5 and y<=-1: 
	    if x>float((0.8-0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.8-0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.5 and x<=0.5 and y>-2 and y<=-1.5: 
	    if x>0:
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<0:
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.7 and x<=0.15 and y>-2.5 and y<=-2: 
	    if x>float((-0.7+0.15)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.7+0.15)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.9 and x<=-0.05 and y>-3 and y<=-2.5: 
	    if x>float((-0.9-0.05)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-0.9-0.05)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.1 and x<=-0.3 and y>-3.5 and y<=-3: 
	    if x>float((-1.1-0.3)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.1-0.3)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.35 and x<=-0.5 and y>=-4 and y<=-3.5: 
	    if x>float((-1.35-0.5)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.35-0.5)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-1.5 and x<=-0.7 and y==-4 : 
	    if x>float((-1.5-0.7)/2):
		    Ag2=float((450+455)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((-1.5-0.7)/2):
		    Ag2=455
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [450 to 445]
    ##########################	
    if x>1.55 and x<=4 and y<=4 and y>3.5: 
	    if x>float((1.55+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.55+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.7 and x<=4 and y>3 and y<=3.5:
	    if x>float((1.7+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.7+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.05 and x<=4 and y>2.85 and y<=3: 
	    if x>float((2.05+4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.05+4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.3 and x<=3.55 and y>2 and y<=2.85: 
	    if  x>float((2.3+3.55)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.3+2.55)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.35 and x<=3.55 and y>1.5 and y<=2: 
	    if x>float((2.35+3.55)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.35+3.55)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.2 and x<=3.34 and y>1 and y<=1.5: 
	    if x>float((2.2+3.34)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.2+3.34)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.85 and x<=3.05 and y>0.5 and y<=1: 
	    if x>float((1.85+3.05)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.85+3.05)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.5 and x<=2.8 and y>0 and y<=0.5: 
	    if x>float((1.5+2.8)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.5+2.8)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.2 and x<=2.4 and y>-0.5 and y<=0: 
	    if x>float((1.2+2.4)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2+2.4)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1 and x<=2.15 and y>-1 and y<=-0.5: 
	    if x>float((2.15+1)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1+2.15)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.8 and x<=2 and y>-1.5 and y<=-1: 
	    if x>float((0.8+2)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.8+2)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.5 and x<=1.8 and y>-2 and y<=-1.5: 
	    if x>float((0.5+1.8)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((0.5+1.8)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.15 and x<=1.45 and y>-2.5 and y<=-2: 
	    if x>float((1.45+0.15)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.45+0.15)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.05 and x<=1.2 and y>-3 and y<=-2.5: 
	    if x>float((1.2-0.05)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.2-0.05)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.3 and x<=0.85 and y>-3.5 and y<=-3: 
	    if x>float((0.85-0.3)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.85-0.3)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.5 and x<=0.6 and y>=-4 and y<=-3.5: 
	    if x>float((0.6-0.5)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.6-0.5)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>-0.7 and x<=0.3 and y==-4 : 
	    if x>float((0.3-0.7)/2):
		    Ag2=float((450+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.3-0.7)/2):
		    Ag2=450
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
		    
    ##########################
    #Raman range [445 to 440]
    ##########################	
    if x==4 and y==2.85: 
	    Ag2=445
	    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x>3.8 and x<=4 and y<2.85 and y>2.5: 
	    if x>float((3.8+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.8+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.55 and x<4 and y>2 and y<=2.5:
	    if x>float((3.55+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.55+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.34 and x<4 and y>1.5 and y<=2: 
	    if x>float((3.34+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.34+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.05 and x<4 and y>1 and y<=1.5: 
	    if  x>float((3.05+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.05+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.8 and x<4 and y>0.5 and y<=1: 
	    if x>float((2.8+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.8+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.4 and x<4 and y>0 and y<=0.5: 
	    if x>float((2.4+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.4+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x>2.15 and x<4 and y>-0.5 and y<=0: 
	    if x>float((2.15+4)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.15+4)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
    
    if x==4 and y==-0.5:
	    Ag2=440
	    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2 and x<3.8 and y>-1 and y<-0.5: 
	    if x>float((2+3.8)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2+3.8)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.8 and x<3.5 and y>-1.5 and y<=-1: 
	    if x>float((1.8+3.5)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.8+3.5)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.45 and x<3.2 and y>-2 and y<=-1.5: 
	    if x>float((3.2+1.45)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.2+1.45)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.2 and x<2.9 and y>-2.5 and y<=-2: 
	    if x>float((2.9+1.2)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.9+1.2)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.85 and x<2.6 and y>-3 and y<=-2.5: 
	    if x>float((2.6+0.85)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((2.6+0.85)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.6 and x<2.2 and y>-3.5 and y<=-3: 
	    if x>float((0.6+2.2)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((0.6+2.2)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>0.3 and x<1.9 and y>=-4 and y<=-3.5: 
	    if x>float((1.9+0.3)/2):
		    Ag2=float((440+445)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.9+0.3)/2):
		    Ag2=445
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    ##########################
    #Raman range [440 to 435]
    ##########################	
    
    if x>3.8 and x<4 and y>-1 and y<-0.5: 
	    if x>float((4+3.8)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+3.8)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.5 and x<4 and y>-1.5 and y<=-1: 
	    if x>float((4+3.5)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+3.5)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>3.2 and x<4 and y>-2 and y<=-1.5: 
	    if x>float((3.2+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((3.2+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.9 and x<4 and y>-2.5 and y<=-2: 
	    if x>float((2.9+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((2.9+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.6 and x<4 and y>-3 and y<=-2.5: 
	    if x>float((2.6+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<float((2.6+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>2.2 and x<4 and y>-3.5 and y<=-3: 
	    if x>float((4+2.2)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((4+2.2)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x>1.9 and x<4 and y>=-4 and y<=-3.5: 
	    if x>float((1.9+4)/2):
		    Ag2=float((440+435)/2)
		    print 'Ag2 peak position: ',Ag2,' cm-1'
	    elif x<=float((1.9+4)/2):
		    Ag2=440
		    print 'Ag2 peak position: ',Ag2,' cm-1'
		    
    if x==4 and y==-4: 
	    Ag2=435
	    print 'Ag2 peak position: ',Ag2,' cm-1'
    m=[]
    r=[]
    n=0
    while n<2001:
	l=300+0.1*n
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
    deltaEgap_4=round(deltaEgap_4,3)
    plt.text(400,5.8,deltaEgap_4,color='blue',fontsize=10)
    plt.text(370,5.8,'delta_Egap4:',color='blue',fontsize=10)
    plt.text(420,5.8,'eV:',color='blue',fontsize=10)    
    plt.text(Ag1-2,5,float(Ag1),color='blue',fontsize=10)
    plt.text(B2g-2,3.5,float(B2g),color='blue',fontsize=10)
    plt.text(Ag2-2,5.4,float(Ag2),color='blue',fontsize=10)
    plt.show()
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

    