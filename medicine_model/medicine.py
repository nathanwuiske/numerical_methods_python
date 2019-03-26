import matplotlib.pyplot as plt
import math
import numpy as np
halflife = 3.2
plasmavolume = 3000
elminiationconstant = math.log(0.5) / halflife
simulationhours = 8
deltaX = 0.08
x = np.arange(0, simulationhours, 0.08)
aspirin = 2 * 325 * 1000
aspirininplasma = [2 * 325 * 1000]
plasma = []

for i in range(0, len(x)):
    elimination = (elminiationconstant * aspirininplasma[i-1] * deltaX)
    aspirininplasma = np.append(aspirininplasma, aspirininplasma[i-1] - elimination)
    plasmaconcentration = aspirininplasma[i-1] / plasmavolume
    plasma = np.append(plasma, plasmaconcentration)




plt.plot(x, plasma)
plt.xlabel('Time')
plt.ylabel('Plasma Concentration')
plt.show()