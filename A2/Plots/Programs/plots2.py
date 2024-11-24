import pandas as pd
import matplotlib.pyplot as plt

randomData = pd.read_csv('randomResults.csv')
reverseData = pd.read_csv('reverseResults.csv')
nearlySortedData = pd.read_csv('nearlySortedResults.csv')

thresholds = [5, 10, 15, 20, 30, 50]
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))
fig.suptitle('Hybrid MergeSort Performance Analysis', fontsize=16, y=0.95)

# Random Arrays
for t in thresholds:
    ax1.plot(randomData['Size'], randomData[f'Hybrid{t}'], linewidth=2, label=f'Threshold={t}')
ax1.set_title('Random Arrays')
ax1.set_xlabel('Array Size')
ax1.set_ylabel('Time (microseconds)')
ax1.grid(True)
ax1.legend()

# Reverse Sorted Arrays
for t in thresholds:
    ax2.plot(reverseData['Size'], reverseData[f'Hybrid{t}'], linewidth=2, label=f'Threshold={t}')
ax2.set_title('Reverse Sorted Arrays')
ax2.set_xlabel('Array Size')
ax2.set_ylabel('Time (microseconds)')
ax2.grid(True)
ax2.legend()

# Nearly Sorted Arrays
for t in thresholds:
    ax3.plot(nearlySortedData['Size'], nearlySortedData[f'Hybrid{t}'], linewidth=2, label=f'Threshold={t}')
ax3.set_title('Nearly Sorted Arrays')
ax3.set_xlabel('Array Size')
ax3.set_ylabel('Time (microseconds)')
ax3.grid(True)
ax3.legend()

plt.tight_layout(pad=3.0)
plt.savefig('hybridSortAnalysis.png', dpi=300, bbox_inches='tight')
plt.close()

# Сравнительный график для размера массива 10000
plt.figure(figsize=(10, 6))
lastSizeIndex = -1

plt.plot([5, 10, 15, 20, 30, 50],
         [randomData[f'Hybrid{t}'].iloc[lastSizeIndex] for t in thresholds],
         label='Random', marker='o')
plt.plot([5, 10, 15, 20, 30, 50],
         [reverseData[f'Hybrid{t}'].iloc[lastSizeIndex] for t in thresholds],
         label='Reverse Sorted', marker='o')
plt.plot([5, 10, 15, 20, 30, 50],
         [nearlySortedData[f'Hybrid{t}'].iloc[lastSizeIndex] for t in thresholds],
         label='Nearly Sorted', marker='o')

plt.title('Hybrid MergeSort Performance by Threshold (Array Size = 10000)')
plt.xlabel('Threshold Value')
plt.ylabel('Time (microseconds)')
plt.legend()
plt.grid(True)

plt.savefig('hybridSortThresholdComparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nStatistics for array size 10000:")
for t in thresholds:
    print(f"\nThreshold = {t}:")
    print(f"Random array: {randomData[f'Hybrid{t}'].iloc[-1]:.2f} microseconds")
    print(f"Reverse sorted array: {reverseData[f'Hybrid{t}'].iloc[-1]:.2f} microseconds")
    print(f"Nearly sorted array: {nearlySortedData[f'Hybrid{t}'].iloc[-1]:.2f} microseconds")