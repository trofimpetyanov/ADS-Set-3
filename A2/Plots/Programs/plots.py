import pandas as pd
import matplotlib.pyplot as plt

random_data = pd.read_csv('randomResults.csv')
reverse_data = pd.read_csv('reverseResults.csv')
nearly_sorted_data = pd.read_csv('nearlySortedResults.csv')

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))
fig.suptitle('MergeSort Performance Analysis', fontsize=16, y=0.95)

# Random Arrays
ax1.plot(random_data['Size'], random_data['MergeSort'], linewidth=2)
ax1.set_title('Random Arrays')
ax1.set_xlabel('Array Size')
ax1.set_ylabel('Time (microseconds)')
ax1.grid(True)

# Reverse Sorted Arrays
ax2.plot(reverse_data['Size'], reverse_data['MergeSort'], linewidth=2)
ax2.set_title('Reverse Sorted Arrays')
ax2.set_xlabel('Array Size')
ax2.set_ylabel('Time (microseconds)')
ax2.grid(True)

# Nearly Sorted Arrays
ax3.plot(nearly_sorted_data['Size'], nearly_sorted_data['MergeSort'], linewidth=2)
ax3.set_title('Nearly Sorted Arrays')
ax3.set_xlabel('Array Size')
ax3.set_ylabel('Time (microseconds)')
ax3.grid(True)

plt.tight_layout(pad=3.0)
plt.savefig('mergesortAnalysis.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 6))
plt.plot(random_data['Size'], random_data['MergeSort'], label='Random', linewidth=2)
plt.plot(reverse_data['Size'], reverse_data['MergeSort'], label='Reverse Sorted', linewidth=2)
plt.plot(nearly_sorted_data['Size'], nearly_sorted_data['MergeSort'], label='Nearly Sorted', linewidth=2)

plt.title('MergeSort Performance Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (microseconds)')
plt.legend()
plt.grid(True)

plt.savefig('mergesortComparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nStatistics for array size 10000:")
print(f"Random array: {random_data['MergeSort'].iloc[-1]:.2f} microseconds")
print(f"Reverse sorted array: {reverse_data['MergeSort'].iloc[-1]:.2f} microseconds")
print(f"Nearly sorted array: {nearly_sorted_data['MergeSort'].iloc[-1]:.2f} microseconds")