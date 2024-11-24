import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('monteCarloResults.csv')

# Area Estimation
plt.figure(figsize=(12, 6))
plt.plot(dataFrame['Points'], dataFrame['WideArea'], label='Wide Area')
plt.plot(dataFrame['Points'], dataFrame['NarrowArea'], label='Narrow Area')
plt.axhline(y=dataFrame['ExactArea'].iloc[0], color='r', linestyle='--', label='Exact Area')
plt.xlabel('Number of Points')
plt.ylabel('Area')
plt.title('Monte Carlo Area Estimation')
plt.legend()
plt.grid(True)
plt.savefig('areaEstimation.png')
plt.close()

# Relative Error
plt.figure(figsize=(12, 6))
wideError = abs(dataFrame['WideArea'] - dataFrame['ExactArea']) / dataFrame['ExactArea'] * 100
narrowError = abs(dataFrame['NarrowArea'] - dataFrame['ExactArea']) / dataFrame['ExactArea'] * 100
plt.plot(dataFrame['Points'], wideError, label='Wide Area Error')
plt.plot(dataFrame['Points'], narrowError, label='Narrow Area Error')
plt.xlabel('Number of Points')
plt.ylabel('Relative Error (%)')
plt.title('Relative Error in Monte Carlo Estimation')
plt.legend()
plt.grid(True)
plt.savefig('relativeError.png')
plt.close()