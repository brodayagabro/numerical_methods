import time
import os
from pylab import *
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
import scipy as sp
import warnings
warnings.filterwarnings('ignore')
clear = lambda: os.system("clear")


# Computational part
# Задание параметров
Lx = Ly = 1.0; Lz=0.1;
T = 0.1
Nx = 50
Ny = 50
Nz = 50
Nt = 100
dx = Lx / Nx
dy = Ly / Ny
dz = Lz / Nz
dt = T / Nt
X = np.linspace(0, Lx, Nx);
Y = np.linspace(0, Ly, Ny);
Z = np.linspace(0, Lz, Nz);
Tset = np.linspace(0, T, Nt);
# Функция, реализующая явную разностную схему для уравнения теплопроводности
def solve_layer(u, a, f, dt, dx, dy, dz):
    unew = u.copy()
    Dxx = 1/dx**2; Dyy = 1/dy**2; Dzz=1/dz**2;
    Nx, Ny, Nz = u.shape
    for k in range(1, Nz - 1):
        for j in range(1, Ny - 1):
            for i in range(1, Nx - 1):
                unew[i, j, k] = u[i, j, k] + dt * (
                    a * (
                        (u[i+1, j, k] - 2*u[i, j, k] + u[i-1, j, k]) * Dxx + 
                        (u[i, j+1, k] - 2*u[i, j, k] + u[i, j-1, k]) * Dyy + 
                        (u[i, j, k+1] - 2*u[i, j, k] + u[i, j, k-1]) * Dyy
                    ) + f[i, j, k]
                )

    # Update Newman conditions
    unew[0, :, :] = unew[1, :, :];
    unew[-1, :, :] = unew[-2, :, :];
    unew[:, 0, :] = unew[:, 1, :];
    unew[:, -1, :] = unew[:, -2, :];
    unew[:, :, 0] = unew[:, :, 1];
    unew[:, :, -1] = unew[:, :, -2];
    return unew


# Инициализация начальных условий
a = 0.05
# Sorce of heat
def f(x, y, z, t):
    if (np.abs(x)>0.7 and np.abs(y)>0.7 and np.abs(z)<0.3): 
        return 5+t
    return 0

def F(TT, dx, dy, dz):
    F_vals = np.zeros((Nt, Nx, Ny, Nz))
    for i in range (1, Nx - 1):
        for j in range(1, Ny-1):
            for k in range(1, Nz-1):
                xi = i*dx; yj = j*dy; zk = k*dz
                if (np.abs(xi)>0.7 and np.abs(yj)>0.7 and np.abs(zk)<0.3):
                    F_vals[:, i, j, k] = f(xi, yj, zk, Tset)

    return F_vals
F_vals = F(Tset, dx, dy, dz)
# Initial conditions
u0 = np.zeros((Nx, Ny, Nz))
for i in range(1, Nx-1):
    for j in range(1, Ny-1):
        u0[i, j, 0:-20] = np.exp(-((X[i]-0.3)**2 + (Y[j]-0.3)**2)/0.1)

def solve():
    U = np.zeros((Nt, Nx, Ny, Nz))
    #U[:, 0, :, :] = U[:, -1, :, :] = U[:, :, 0, :] = U[:, :, -1, :] = U[:, :, :, 0] = U[:, :, :, -1]
    u = np.copy(u0)
    U[0] = u0
    for n in range(1, Nt):
        clear()
        print(f'Progress: {round(n/(Nt), 2)*100}%')  
        u = solve_layer(u, a, F_vals[n], dt, dx, dy, dz)
        U[n] = u
    return U

U = solve()

# Drawing part
# Create a subplot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
 
# Create 3 axes for 3 sliders red,green and blue
axn = fig.add_axes([0.25, 0.2, 0.65, 0.03])
axk = fig.add_axes([0.25, 0.15, 0.65, 0.03])
 
n0 = 30
k0 = 30

n = Slider(axn, 'n', 0, 100, 30)
 
k = Slider(axk, 'k', 0, 100, 30)

 
# Create function to be called when slider value is changed
# Создание интерактивного интерфейса
def displayZT(n, k, U):
    n = int(round(n/100*Nz, 0))
    if n>Nz-1:
        n = Nz-1
    k = int(round(k/100*Nt, 0))
    if k>Nt-1:
        k = Nt-1
    c = ax.imshow(U[k, :, :, n],cmap='coolwarm')
    #plt.colorbar(c)
    #ax.contour(X,Y,U[k, :, :, n],10,colors='k')
    #plt.clabel(cp1,inline=True, fontsize=10)
    return None

displayZT(n0, k0, U)

def update(val):
    global k, n
    k_val = k.val
    n_val = n.val
    n_val = int(round(n_val/100*Nz, 0))
    if n_val>Nz-1:
        n_val = Nz-1
    k_val = int(round(k_val/100*Nt, 0))
    if k_val>Nt-1:
        k_val = Nt-1
    c = ax.imshow(U[k_val, :, :, n_val],cmap='coolwarm')
 
# Call update function when slider value is changed
k.on_changed(update)
n.on_changed(update)
 
plt.show()