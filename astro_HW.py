import numpy as np
import matplotlib.pyplot as plt

# constants
c = 3e8 # speed of light (m/s)
h = 6.626e-34 # Planck's constant (J*s)
k = 1.38e-23 # Boltzmann's constant (Joules/Kelvin)

# HW 3 problem 2.5

l = np.linspace(0.3, 10, 500) # x axis; 0.3 to 10 microns
T_1, T_2 = 3000, 3100
def B_l(l, t):
    wavelength = l*1e-6
    B = (2*h)*(c**2)/((wavelength**5)*(np.e**((h*c)/(wavelength*k*t)) - 1))
    return B*1e-12


plt.plot(l, B_l(l, T_1), color='b', linestyle='--', label='3000 K')
plt.plot(l, B_l(l, T_2), color='r', label='3100 K')
plt.legend()
plt.title("Blackbody emission curve for 3000 K and 3100 K bodies")
plt.xlabel("Wavelength λ (microns)")
plt.ylabel("B_λ(T) (10^4 W m^-2 nm^-1 sr^-1)")

plt.show()

polynomial_coefficients = [1, -1, -6]
print(np.roots(polynomial_coefficients))