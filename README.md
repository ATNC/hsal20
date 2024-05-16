
## Performance Comparison of BBST Operations
   
   | Dataset Size | Avg. Insert Time (seconds) | Avg. Delete Time (seconds) | Avg. Search Time (seconds) |
   |--------------|----------------------------|----------------------------|---------------------------|
   | 100          | 0.003627                   | 0.003278                   | 0.000058                  |
   | 500          | 0.091356                   | 0.088607                   | 0.000410                  |
   | 1000         | 0.373744                   | 0.367470                   | 0.000933                  |

### Conclusions:
- The average time for all operations (insert, delete, search) increases as the size of the dataset increases. This is expected as larger datasets require more computational resources to process.
- The insert and delete operations have similar average times for each dataset size, suggesting that these operations have similar complexities in the BBST implementation.
- The search operation is significantly faster than the insert and delete operations. This is likely due to the balanced nature of the BBST, which ensures a maximum height logarithmic in the number of elements, making search operations efficient.

## When counting sort doesn't perform?
Counting Sort is a non-comparison-based sorting algorithm that works well when the range of input values (k) is not significantly greater than the number of elements (n) in the input array. However, Counting Sort doesn't perform well in the following scenarios:

Large Range of Input Values: If the range of input values (k) is much larger than the number of elements (n) in the array, Counting Sort requires extra space proportional to the range of values. This can lead to inefficient memory usage, especially if the range of values is very large.

Non-Integer Inputs: Counting Sort is typically designed for sorting integers. If the input array contains non-integer elements or floating-point numbers, Counting Sort may not be directly applicable without some preprocessing to map these elements to integers.

Sparse Input Arrays: If the input array contains a lot of empty or sparsely populated elements within the range, Counting Sort still allocates memory for each possible value in the range. This can lead to inefficient memory usage and decreased performance compared to other sorting algorithms.

Performance with Negative Values: Counting Sort typically assumes non-negative integer inputs. While it's possible to adapt Counting Sort to handle negative values by shifting the range, this introduces additional complexity and may affect performance.

Stability Requirement: Counting Sort is not inherently stable. If stability in sorting identical elements is required, additional steps need to be taken to ensure stability, which can increase the complexity of the algorithm.

In these scenarios, other sorting algorithms like Merge Sort, Quick Sort, or Heap Sort may be more suitable and efficient.