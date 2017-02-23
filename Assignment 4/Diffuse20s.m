clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
z=1;
sq=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%   prestine  x cordinations        %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:6
    xxxx(n)=2.1e-4-(2e-8)*(n-1);
end

% origin concentration 

for b=2.1e-4:-2e-8:2.099e-4
    cccc(sq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sq=sq+1;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%% t=20 s s%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%x cordinations     
for n=1:1:57
    xxxx(n)=2.1e-4-(2e-8)*(n-1);
end

%origin concentration (y axis)
for b=2.1e-4:-2e-8:2.099e-4
    cccc(sq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    sq=sq+1;
end

for k=7:1:57
    cccc(k)=0;
end
for z=1:1:(10/0.001)
    for s=2:1:56
        cccc(s)=cccc(s)+D*0.001*(cccc(s-1)+cccc(s+1)-2*cccc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end

plot(xxxx,cccc,'*b','LineWidth',2);
axis([2.088e-4 2.100e-4 1e15 1.5e18]);