clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
se=1;
z=1;
sq=1;
qs=1;
ee=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);


%%%%%%%%%%%%%%%%%%%%%%%%%     x axis  (width)      %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:68
    tx(n)=2.1e-4-(2e-8)*(n-1);
end
for n=68:-1:1
    wj(qs)=tx(n);
    qs=qs+1;
end
for n=1:1:267
    wj(qs)=2.1e-4+(2e-8)*(n);
    qs=qs+1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%% y axis (concentration) %%%%%%%%%%%%%%%%%%%%%%
for b=2.099e-4:2e-8:2.1e-4
    sc(sq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sq=sq+1;
end
for b=2.1002e-4:2e-8:2.14e-4
    sc(sq)=1e18;
    sq=sq+1;
end
for b=2.1402e-4:2e-8:2.141e-4
    sc(sq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sq=sq+1;
end
for sp=1:1:62
    ic(sp)=0;
end
for sp=63:1:273
    ic(sp)=sc(ee);
    ee=ee+1;
end
for sp=274:1:335
    ic(sp)=0;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Diffusion  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(30/0.001)
    for s=2:1:334
        ic(s)=ic(s)+D*0.001*(ic(s-1)+ic(s+1)-2*ic(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
plot(wj,ic,'--*','LineWidth',2);
axis([2.087e-4 2.152e-4 1e15 1.5e18]);








