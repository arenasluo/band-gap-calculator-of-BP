clear all
close all 
clc
data1=load('ag1_346.txt')
F1=data1(:,1)
F2=data1(:,2)

data2=load('ag1_350.txt')
F3=data2(:,1)
F4=data2(:,2)

data3=load('ag1_354.txt')
F5=data3(:,1)
F6=data3(:,2)

data4=load('ag1_358.txt')
F7=data4(:,1)
F8=data4(:,2)

data5=load('ag1_362.txt')
F9=data5(:,1)
F10=data5(:,2)

data6=load('ag1_366.txt')
F11=data6(:,1)
F12=data6(:,2)

data7=load('ag1_370.txt')
F13=data7(:,1)
F14=data7(:,2)

data8=load('ag1_374.txt')
F15=data8(:,1)
F16=data8(:,2)

data9=load('ag1_378.txt')
F17=data9(:,1)
F18=data9(:,2)


%plot(F1,F2,'r*',F1,F2,'b-','Markersize',8,'linewidth',0.1)%'.','Markersize',20,)
plot(F1,F2,'o','linewidth',1)%'.','Markersize',20,)
hold on
plot(F3,F4,'r-','linewidth',1)%'.','Markersize',20,)
hold on
plot(F5,F6,'y','linewidth',1)%'.','Markersize',20,)
hold on
plot(F7,F8,'g','linewidth',1)%'.','Markersize',20,)
hold on
plot(F9,F10,'c','linewidth',1)%'.','Markersize',20,)
hold on 
plot(F11,F12,'b','linewidth',1)%'.','Markersize',20,)
hold on 
plot(F13,F14,'m','linewidth',1)%'.','Markersize',20,)
hold on
plot(F15,F16,'k','linewidth',1)%'.','Markersize',20,)
hold on
plot(F17,F18,'*','linewidth',1)%'.','Markersize',20,)
axis([-4 4 -4 4])
%legend('p','fit');
a=[F17(end:-1:1),F18(end:-1:1);F15,F16]
b=[F15(end:-1:1),F16(end:-1:1);F13,F14]
c=[F13(end:-1:1),F14(end:-1:1);F11,F12]
d=[F11(end:-1:1),F12(end:-1:1);F9,F10]
e=[F9,F10;F7(end:-1:1),F8(end:-1:1)]
f=[F7,F8;F5(end:-1:1),F6(end:-1:1)]
g=[F5,F6;F3(end:-1:1),F4(end:-1:1)]
h=[F3,F4;F1,F2]
fill(a(:,1),a(:,2),'r')
fill(b(:,1),b(:,2),[1 0.5 0])
fill(c(:,1),c(:,2),'y')
fill(d(:,1),d(:,2),[0 1 0])%green
fill(e(:,1),e(:,2),[0 1 0.5])
fill(f(:,1),f(:,2),[0 1 1])%cyan
fill(g(:,1),g(:,2),[0 0.5 1])
fill(h(:,1),h(:,2),[0 0 1])
grid on
set(gca,'XTick',-4:0.5:4,'XMinorTick','on')
set(gca,'YTick',-4:0.5:4,'YMinorTick','on')
xlabel('x zigzag (%)')%%!!!!it's xlabel!!!
ylabel('y armchair (%)')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

