import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('vtc_5v.csv', sep='\t')
vin = df.iloc[:, 0].values
vout = df.iloc[:, 1].values

# switching threshold: where Vout = 2.5 V (reverse because vout falls)
vm = np.interp(2.5, vout[::-1], vin[::-1])

plt.figure(figsize=(6, 4))
plt.plot(vin, vout, label='Discrete CMOS inverter')
plt.axhline(2.5, ls='--', color='gray')
plt.axvline(vm, ls='--', color='red', label=f'Vm = {vm:.2f} V')
plt.xlabel('VIN (V)')
plt.ylabel('VOUT (V)')
plt.title('Voltage transfer characteristic')
plt.grid(True)
plt.legend()
plt.savefig('vtc.png', dpi=300, bbox_inches='tight')
plt.show()