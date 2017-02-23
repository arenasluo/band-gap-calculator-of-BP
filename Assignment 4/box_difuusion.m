clc; 
clear all
x=2100:0.5:2141;
c=1e15
y=c;
plot(x,y,'--*r','linewidth',1)
axis([2090 2150 0 1.5e15])
hold on;
%plot(2100*ones(1,2),ylim,'r:');%??????
%plot(2140*ones(1,2),ylim,'r:');%??????
%grid on