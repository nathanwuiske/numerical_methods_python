from math import log
import matplotlib.pyplot as plt
import numpy as np
def xtoi(x):
    return x / deltaX

def itox(i):
    return (i - 1) * deltaX

mec = 10
mtc = 20
halfLife = 22
volume = 3000
dosage = 100 * 1000
absorptionFraction = 0.12
interval = 8

eliminationConstant = -log(0.5) / halfLife
druginSystem = [absorptionFraction * dosage]
simHrs = 168
deltaX = 0.03
concentration = []

x = np.arange(0, simHrs, 0.033333)
print(x)
for i in range(0, len(x)):
    if itox(i) % interval == 0:
        ingested = absorptionFraction * dosage
    else:
        ingested = 0
    eliminated = (eliminationConstant * druginSystem[i-1]) * deltaX
    druginSystem = np.append(druginSystem, druginSystem[i-1] + ingested - eliminated)
    con = druginSystem / volume
    concentration = np.append(concentration, con)


plt.plot(x, concentration)
#plt.xlabel('Time')
plt.show()
