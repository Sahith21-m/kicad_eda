import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Load and Scale Dataset 1 (Divided by 5) ---
df1 = pd.read_csv('vtc_5v.csv', sep='\t')
vin1 = df1.iloc[:, 0].values / 5.0
vout1 = df1.iloc[:, 1].values / 5.0
vm1 = np.interp(2.5 / 5.0, vout1[::-1], vin1[::-1])  # Scaled threshold reference

# --- Load and Scale Dataset 2 (Divided by 1.1) ---
df2 = pd.read_csv('s7_data.csv', sep='\t') 
vin2 = df2.iloc[:, 0].values / 1.1
vout2 = df2.iloc[:, 1].values / 1.1
vm2 = np.interp(2.5 / 1.1, vout2[::-1], vin2[::-1])  # Scaled threshold reference

# --- Plotting Both ---
plt.figure(figsize=(6, 4))

# Plot Dataset 1
plt.plot(vin1, vout1, label='Discrete (Scaled /5)')
plt.axvline(vm1, ls='--', color='red', alpha=0.7, label=f'Vm1 = {vm1:.2f} V')

# Plot Dataset 2
plt.plot(vin2, vout2, label='65nm_inverter (Scaled /1.1)')
plt.axvline(vm2, ls=':', color='blue', alpha=0.7, label=f'Vm2 = {vm2:.2f} V')

plt.xlabel('VIN (Scaled V)')
plt.ylabel('VOUT (Scaled V)')
plt.title('Overlay Scaled Voltage Transfer Characteristics')
plt.grid(True)
plt.legend()
plt.savefig('vtc_overlay_scaled.png', dpi=300, bbox_inches='tight')
plt.show()