clc; 
clear all
D=1.2662e-14; % diffusivity @ 1000 C 
r=1;
s=1;
z=1;
qq=1;e=1;
n=1;% counter
u=(1e15-1e18)/(4.1e-13);

%%%%%%%%%%%%%%%%%%%%%%%%%     x axis  (width)      %%%%%%%%%%%%%%%%%%%%%%%
for b=2.099e-4:2e-8:2.1e-4
    cc(qq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    qq=qq+1;
end
for b=2.1002e-4:2e-8:2.14e-4
    cc(qq)=1e18;
    qq=qq+1;
end
for b=2.1402e-4:2e-8:2.141e-4
    cc(qq)=u*(b-2.12e-4).^2+1e15-u*(2.1e-6)^2;
    qq=qq+1;
end
for n=1:1:31
    xx(n)=2.1e-4-(2e-8)*(n-1);
end
for n=31:-1:1
    jj(s)=xx(n);
    s=s+1;
end
for n=1:1:232
    jj(s)=2.1e-4+(2e-8)*(n);
    s=s+1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%% y axis (concentration) %%%%%%%%%%%%%%%%%%%%%%
for pp=1:1:31
    fc(pp)=0;
end
for pp=32:1:231
    fc(pp)=cc(e);
    e=e+1;
end
for pp=232:1:263
    fc(pp)=0;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Diffusion  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for z=1:1:(5/0.001)
    for s=2:1:262
        fc(s)=fc(s)+D*0.001*(fc(s-1)+fc(s+1)-2*fc(s))/((2e-8)^2);%2e-8 cm,0.2nm
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

plot(jj,fc,'--o','LineWidth',2);
axis([2.09e-4 2.147e-4 1e15 1.5e18]);



