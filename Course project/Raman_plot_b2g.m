clear all
close all 
clc
data1=load('b2g_390.txt')
E1=data1(:,1)
E2=data1(:,2)

data2=load('b2g_400.txt')
E3=data2(:,1)
E4=data2(:,2)

data3=load('b2g_410.txt')
E5=data3(:,1)
E6=data3(:,2)

data4=load('b2g_419.txt')
E7=data4(:,1)
E8=data4(:,2)

data5=load('b2g_428.txt')
E9=data5(:,1)
E10=data5(:,2)

data6=load('b2g_438.txt')
E11=data6(:,1)
E12=data6(:,2)

data7=load('b2g_447.txt')
E13=data7(:,1)
E14=data7(:,2)

data8=load('b2g_456.txt')
E15=data8(:,1)
E16=data8(:,2)

data9=load('b2g_465.txt')
E17=data9(:,1)
E18=data9(:,2)


%plot(E1,E2,'r*',E1,E2,'b-','Markersize',8,'linewidth',0.1)%'.','Markersize',20,)
plot(E1,E2,'o','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E3,E4,'r-','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E5,E6,'y','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E7,E8,'g','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E9,E10,'c','linewidth',0.1)%'.','Markersize',20,)
hold on 
plot(E11,E12,'b','linewidth',0.1)%'.','Markersize',20,)
hold on 
plot(E13,E14,'m','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E15,E16,'k','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(E17,E18,'-','linewidth',0.1)%'.','Markersize',20,)
axis([-4 4 -4 4])
a=[E17(end:-1:1),E18(end:-1:1);E15,E16]
b=[E15(end:-1:1),E16(end:-1:1);E13,E14]
c=[E13,E14;E11,E12]
d=[E11,E12;E9,E10]
e=[E9,E10;E7(end:-1:1),E8(end:-1:1)]
f=[E7,E8;E5(end:-1:1),E6(end:-1:1)]
g=[E5,E6;E3(end:-1:1),E4(end:-1:1)]
h=[E3,E4;E1,E2]
fill(a(:,1),a(:,2),'r')
fill(b(:,1),b(:,2),[1 0.5 0])
fill(c(:,1),c(:,2),'y')
fill(d(:,1),d(:,2),[0 1 0])%green
fill(e(:,1),e(:,2),[0 1 0.5])
fill(f(:,1),f(:,2),[0 1 1])%cyan
fill(g(:,1),g(:,2),[0 0.5 1])
fill(h(:,1),h(:,2),[0 0 1])
%legend('p','fit');



%fill(a,b,'b')
set(gca,'XTick',-4:0.5:4,'XMinorTick','on')
set(gca,'YTick',-4:0.5:4,'YMinorTick','on')
xlabel('x zigzag (%)')%%!!!!it's xlabel!!!
ylabel('y armchair (%)')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
grid on 
