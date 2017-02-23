clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
z=1;
tq=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%   prestine  x cordinations        %%%%%%%%%%%%%%%%%%%%%%%
% origin concentration 

for b=2.1e-4:-2e-8:2.099e-4
    ccc(tq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    tq=tq+1;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%% t=10 s s%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%x cordinations     
for n=1:1:43
    xxx(n)=2.1e-4-(2e-8)*(n-1);
end

%origin concentration (y axis)
for b=2.1e-4:-2e-8:2.099e-4
    ccc(tq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    tq=tq+1;
end

for k=7:1:43
    ccc(k)=0;
end


for z=1:1:(10/0.001)
    for s=2:1:42
        ccc(s)=ccc(s)+D*0.001*(ccc(s-1)+ccc(s+1)-2*ccc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end

plot(xxx,ccc,'--c','LineWidth',2);
axis([2.091e-4 2.100e-4 1e16 1.5e18]);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

