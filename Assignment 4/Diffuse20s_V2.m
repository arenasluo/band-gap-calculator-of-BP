clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
se=1;
z=1;
sm=1;
rs=1;
re=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%     x axis  (width)      %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:57
    tx(n)=2.1e-4-(2e-8)*(n-1);
end
for n=57:-1:1
    uj(rs)=tx(n);
    rs=rs+1;
end
for n=1:1:256
    uj(rs)=2.1e-4+(2e-8)*(n);
    rs=rs+1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%% y axis (concentration) %%%%%%%%%%%%%%%%%%%%%%
for b=2.099e-4:2e-8:2.1e-4
    sc(sm)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sm=sm+1;
end
for b=2.1002e-4:2e-8:2.14e-4
    sc(sm)=1e18;
    sm=sm+1;
end
for b=2.1402e-4:2e-8:2.141e-4
    sc(sm)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sm=sm+1;
end
for sp=1:1:51
    hc(sp)=0;
end
for sp=51:1:261
    hc(sp)=sc(re);
    re=re+1;
end
for sp=262:1:313
    hc(sp)=0;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Diffusion  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(20/0.001)
    for s=2:1:312
        hc(s)=hc(s)+D*0.001*(hc(s-1)+hc(s+1)-2*hc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
plot(uj,hc,'o','LineWidth',2);
axis([2.087e-4 2.152e-4 1e15 1.5e18]);






