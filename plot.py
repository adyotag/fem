import numpy as np
from matplotlib import pyplot as plt

sigma_xx_11 = [-2.,0.,2.]
sigma_xx_12 = [-1.6383,0.0003,1.6383]
sigma_xx_22 = [-1.45,0.0,1.45]
y = np.asarray([0.,0.005,0.01])
analytical = 600. *(y-.005)


plt.plot(y, sigma_xx_11, label='1x1 Gaussian Quadrature')
plt.plot(y, sigma_xx_12, label='1x2 Gaussian Quadrature')
plt.plot(y, sigma_xx_22, label='2x2 Gaussian Quadrature')
plt.plot(y, analytical, label='Analytical')
plt.title(r'Plot of $\sigma_{xx}$ along a vertical line in the middle of the beam')
plt.xlabel('y position (m)')
plt.ylabel('Stress (MPa)')
plt.legend()
plt.show()
