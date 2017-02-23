clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
z=1;
qq=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%   prestine  x cordinations        %%%%%%%%%%%%%%%
for b=2.1e-4:-2e-8:2.099e-4
    cc(qq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    qq=qq+1;
end

%origin concentration (y axis)
for b=2.1e-4:-2e-8:2.099e-4
    cc(qq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    qq=qq+1;
end

for k=7:1:32
    cc(k)=0;
end

% X axis
for n=1:1:32
    xx(n)=2.1e-4-(2e-8)*(n-1);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Diffusion  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(5/0.001)
    for s=2:1:31
        cc(s)=cc(s)+D*0.001*(cc(s-1)+cc(s+1)-2*cc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



plot(xx,cc,'r','LineWidth',2);
axis([2.093e-4 2.100e-4 1e16 1.5e18]);