
for t=0:1:5
    for i=2:41999
        g=D*t*(b(1,i)-2*b(1,i+1)+b(1,i+2))/(c^2);
        b(i)=b(i)+g;
    end
end
plot(a,b,'r','linewidth',2)
axis([2099 2100 0 1.5e15])
hold on;
plot(2100*ones(1,2),ylim,'r:');
plot(2140*ones(1,2),ylim,'r:');
grid on
