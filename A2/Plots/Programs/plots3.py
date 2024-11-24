import pandas as pd
import matplotlib.pyplot as plt

randomData = pd.read_csv('randomResults.csv')
reverseData = pd.read_csv('reverseResults.csv')
nearlySortedData = pd.read_csv('nearlySortedResults.csv')

plt.figure(figsize=(12, 6))
plt.plot(randomData['Size'], randomData['MergeSort'], label='MergeSort (Random)', linewidth=2)
plt.plot(randomData['Size'], randomData['Hybrid50'], label='HybridSort (Random)', linewidth=2)
plt.plot(nearlySortedData['Size'], nearlySortedData['MergeSort'], label='MergeSort (Nearly Sorted)', linewidth=2)
plt.plot(nearlySortedData['Size'], nearlySortedData['Hybrid50'], label='HybridSort (Nearly Sorted)', linewidth=2)

plt.title('MergeSort vs HybridSort Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (microseconds)')
plt.legend()
plt.grid(True)

plt.savefig('mergeVsHybrid.png', dpi=300, bbox_inches='tight')
plt.close()