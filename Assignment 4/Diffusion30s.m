clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
z=1;
pq=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%   prestine  x cordinations        %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:6
    xxxxx(n)=2.1e-4-(2e-8)*(n-1);
end

% origin concentration 

for b=2.1e-4:-2e-8:2.099e-4
    ccccc(pq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    pq=pq+1;
end

%%%%%%%%%%%1%%%%%%%%%%%%%%%%%% t=30 s s%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%x cordinations     
for n=1:1:68
    xxxxx(n)=2.1e-4-(2e-8)*(n-1);
end

%origin concentration (y axis)
for b=2.1e-4:-2e-8:2.099e-4
    ccccc(pq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    pq=pq+1;
end

for k=7:1:68
    ccccc(k)=0;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(10/0.001)
    for s=2:1:67
        ccccc(s)=ccccc(s)+D*0.001*(ccccc(s-1)+ccccc(s+1)-2*ccccc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end

plot(xxxxx,ccccc,'--o','LineWidth',2);
axis([2.085e-4 2.100e-4 1e15 1.5e18]);