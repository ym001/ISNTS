#source:https://informatique-python.readthedocs.io/fr/latest/Exercices/canon.html
import numpy as N
import scipy.integrate as SI
import matplotlib.pyplot as plt
g = 9.81        # Pesanteur [m/s2]
cx = 0.45       # Coefficient de frottement d'une sphère
rhoAir = 1.2    # Masse volumique de l'air [kg/m3] au niveau de la mer, T=20°C
rad = 0.1748/2  # Rayon du boulet [m]
rho = 6.23e3    # Masse volumique du boulet [kg/m3]
mass = 4./3.*N.pi*rad**3 * rho            # Masse du boulet [kg]
alpha = 0.5*cx*rhoAir*N.pi*rad**2 / mass  # Coefficient de frottement par unité de masse
print("Masse du boulet: {:.2f} kg".format(mass))
print("Coefficient de frottement par unité de masse: {} S.I.".format(alpha))
v0 = 450.           # Vitesse initiale [m/s]
alt = 45.           # Inclinaison du canon [deg]
alt *= N.pi / 180.  # Inclinaison [rad]
z0 = (0., 0., v0 * N.cos(alt), v0 * N.sin(alt)) # (x0, y0, vx0, vy0)
tc = N.sqrt(mass / (g * alpha))
print("Temps caractéristique: {:.1f} s".format(tc))
t = N.linspace(0, tc, 100)
def zdot(z, t):
    """Calcul de la dérivée de z=(x, y, vx, vy) à l'instant t."""

    x, y, vx, vy = z
    alphav = alpha * N.hypot(vx, vy)

    return (vx, vy, -alphav * vx, -g - alphav * vy) # dz/dt = (vx,vy,x..,y..)
zs = SI.odeint(zdot, z0, t)
ypos = zs[:,1]>=0 # y>0?
print("temps de coll. t(y~0) = {:.0f} s".format(t[ypos][-1])) # Dernier instant pour lequel y>0
print("portée x(y~0) = {:.0f} m".format(zs[ypos, 0][-1])) # Portée approximative du canon
#print "y(y~0) = {:.0f} m".format(zs[ypos, 1][-1]) # ~0
print("vitesse(y~0): {:.0f} m/s".format(N.hypot(zs[ypos, 2][-1], zs[ypos, 3][-1])))

plt.plot(zs[ypos, 0], zs[ypos, 1])
plt.ylabel('x [m]')
plt.xlabel("y [m]")
plt.show()
