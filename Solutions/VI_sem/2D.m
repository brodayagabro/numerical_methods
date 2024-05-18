clc; clear all
Nx = 100; Ny = 100; t_end = 10000; Lx = 30;
Ly = 40; lamda = 45.5; rho = 8800; C = 384; Th = 80;
Tc = 30; T0 = -5; hx = Lx/(Nx-1); hy = Ly/(Ny-1);
at = lamda/(rho*C);  tau = t_end/1000;
 
for i = 1:Nx
    for j = 1:Ny
        T(i,j) = T0;
    end
end
 
time = 0;
 
while time<t_end
    
    time = time + tau;
    
    for j = 1:Ny
        alfa(1) = 0;
        beta(1) = Th;
        for i = 2:Nx-1
            a(i) = lamda/hx^2;
            b(i) = 2.0*lamda/hx^2+rho*C/tau;
            c(i) = lamda/hx^2;
            f(i) = -rho*C*T(i,j)/tau;
            
            alfa(i) = a(i)/(b(i)-c(i)*alfa(i-1));
            beta(i) = (c(i)*beta(i-1)-f(i))/(b(i)-c(i)*alfa(i-1));
        end
        
        T(Nx,j) = Tc;
        
        for i = Nx-1:-1:1
            T(i,j) = alfa(i)*T(i+1,j)+beta(i);
        end
    end
    for i = 2:Nx-1
        alfa(1) = 2.0*at*tau/(2.0*at*tau+hy^2);
        beta(1) = hy^2*T(i,1)/(2.0*at*tau+hy^2);
        for j = 2:Ny-1
            a(i) = lamda/hy^2;
            b(i) = 2.0*lamda/hy^2+rho*C/tau;
            c(i) = lamda/hy^2;
            f(i) = -rho*C*T(i,j)/tau;
            
            alfa(j) = a(i)/(b(i)-c(i)*alfa(j-1));
            beta(j) = (c(i)*beta(j-1)-f(i))/(b(i)-c(i)*alfa(j-1));
        end
        
        T(i,Ny) = (2.0*at*tau*beta(Ny-1)+hy^2*T(i,Ny))/(2.0*at*tau*(1.0-alfa(Ny-1))+hy^2);
        
        for j = Ny-1:-1:1
            T(i,j) = alfa(j)*T(i,j+1)+beta(j);
        end
    end;