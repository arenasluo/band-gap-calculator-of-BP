clear all
close all 
clc
data1=load('ag2_435.txt')
H1=data1(:,1)
H2=data1(:,2)

data2=load('ag2_440.txt')
H3=data2(:,1)
H4=data2(:,2)

data3=load('ag2_445.txt')
H5=data3(:,1)
H6=data3(:,2)

data4=load('ag2_450.txt')
H7=data4(:,1)
H8=data4(:,2)

data5=load('ag2_455.txt')
H9=data5(:,1)
H10=data5(:,2)

data6=load('ag2_460.txt')
H11=data6(:,1)
H12=data6(:,2)

data7=load('ag2_465.txt')
H13=data7(:,1)
H14=data7(:,2)

data8=load('ag2_470.txt')
H15=data8(:,1)
H16=data8(:,2)

data9=load('ag2_476.txt')
H17=data9(:,1)
H18=data9(:,2)


%plot(H1,H2,'r*',H1,H2,'b-','Markersize',8,'linewidth',0.1)%'.','Markersize',20,)
plot(H1,H2,'o','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H3,H4,'r-','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H5,H6,'y','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H7,H8,'g','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H9,H10,'c','linewidth',0.1)%'.','Markersize',20,)
hold on 
plot(H11,H12,'b','linewidth',0.1)%'.','Markersize',20,)
hold on 
plot(H13,H14,'m','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H15,H16,'k','linewidth',0.1)%'.','Markersize',20,)
hold on
plot(H17,H18,'*','linewidth',0.1)%'.','Markersize',20,)
axis([-4 4 -4 4])
%legend('p','fit');
a=[H17(end:-1:1),H18(end:-1:1);H15,H16]
b=[H15(end:-1:1),H16(end:-1:1);H13,H14]
c=[H13(end:-1:1),H14(end:-1:1);H11,H12]
d=[H11(end:-1:1),H12(end:-1:1);H9,H10]
e=[H9,H10;H7(end:-1:1),H8(end:-1:1)]
f=[H7,H8;H5(end:-1:1),H6(end:-1:1)]
g=[H5,H6;H3(end:-1:1),H4(end:-1:1)]
h=[H3,H4;H1,H2]
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

