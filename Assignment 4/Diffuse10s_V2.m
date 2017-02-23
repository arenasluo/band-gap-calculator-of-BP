clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
ts=1;
te=1;
z=1;
tq=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%     x axis  (width)      %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:42
    tx(n)=2.1e-4-(2e-8)*(n-1);
end
for n=42:-1:1
    tj(ts)=tx(n);
    ts=ts+1;
end
for n=1:1:241
    tj(ts)=2.1e-4+(2e-8)*(n);
    ts=ts+1;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%% y axis (concentration) %%%%%%%%%%%%%%%%%%%%%%
for b=2.099e-4:2e-8:2.1e-4
    tc(tq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    tq=tq+1;
end
for b=2.1002e-4:2e-8:2.14e-4
    tc(tq)=1e18;
    tq=tq+1;
end
for b=2.1402e-4:2e-8:2.141e-4
    tc(tq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    tq=tq+1;
end
for tp=1:1:36
    gc(tp)=0;
end
for tp=37:1:247
    gc(tp)=tc(te);
    te=te+1;
end
for tp=248:1:283
    gc(tp)=0;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Diffusion  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(10/0.001)
    for s=2:1:282
        gc(s)=gc(s)+D*0.001*(gc(s-1)+gc(s+1)-2*gc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
plot(tj,gc,'.c','LineWidth',2);
axis([2.09e-4 2.15e-4 1e15 1.5e18]);

