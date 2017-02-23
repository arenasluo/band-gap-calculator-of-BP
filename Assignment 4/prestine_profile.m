(* ::Package:: *)

% pristine profile
clc; 
clear all
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Now t=5
% Upper diffusion starts from x=2100, lower diffusion starts from x=2140
% since the lowest time t=5s, diffusion legnth (L) =5.03e-7 cm >> 1nm (the
% gap between Cp and Cmax), grid mesh by diffusion length at each time step
% select time step delta(t)=0.001, because L=2*sqrt(D*0.001)=0.0712nm <<1nm,
% we can neglect the diffusion fronts,the left boundary we set was at
% x=2.1e-4-2*sqrt(D*5)=2094.97; the right boundary we set was at
% x=2.14e-4+2*sqrt(D)*5=2145.03

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% Predifination %%%%%%%%%%%%%%%%%%
D=1.2662e-14; % diffusivity @ 1000 C 
 % t=5, timestep=0.001
t=5;
r=1;s=1;z=1;q=1;n=1;% counter

%%%%%%%%%%%%%%%%%%%%%%%%%   prestine  x cordinations        %%%%%%%%%%%%%%%%%%%%%%%
for n=1:1:6
    x(n)=2.1e-4-(2e-8)*(n-1);
end
for b=6:-1:1
    j(z)=x(n);
    z=z+1;
    n=n-1;
end
for r=1:1:205
    j(z)=2.1e-4+(2e-8)*(r);
    z=z+1;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%% origin concentration %%%%%%%%%%%%%%%%%%%%%%%%%
u=(1e15-1e18)/(4.1e-13);
for b=2.1e-4:-2e-8:2.099e-4
    c(q)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    q=q+1;
end

for b=6:-1:1
    o(s)=c(b);
    s=s+1;
end
for b=7:1:206
    o(b)=1e18;
end
for b=207:1:211
    o(b)=c(b-205);
end

plot(j,o,'r','LineWidth',2);
axis([2.09e-4 2.150e-4 1e15 1.5e18]);
