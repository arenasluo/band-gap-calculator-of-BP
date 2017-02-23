clear all;
clc;

e0=-8.6288;
e1=3.507;
e2=0.411;
syms E;
ex=rand;
ey=rand;
ez=rand;
syms e;
syms phai;
syms psai;
gama=rand;
int m;
e=sqrt((ex-ey)^2+(2*gama)^2);
tan(psai)=(2*gama)/(ex-ey);
phai=-(psai)/2+(m)*pi/2;
E=e0*ez+(e1-2*e2)*(ex+ey)-2*(e2)*e*cos(2*phai+psai);

%For uniaxial strain in the z direction, i.e., ?x=?y=0, ?=0,and ?z?0:
