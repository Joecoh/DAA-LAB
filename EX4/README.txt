Transform and Conquer - Heap Sort

Heap Sort is an in-place sorting algorithm that is based on the binary heap data structure. It follows the "Transform and Conquer" approach, where the problem is transformed into a simpler instance, and the solution to the simpler instance is then transformed to solve the original problem.

Here's a brief overview of how Heap Sort works:

1)Build Heap: Convert the array into a max-heap (or min-heap) to satisfy the heap property. This is the     "transform" step.
2)Sort Heap: Swap the root (the maximum element for max-heap or the minimum element for min-heap) with the last element of the heap. Reduce the heap size by 1 and heapify the root. Repeat this process until the heap is empty. This is the "conquer" step.

Here heapify is a function to heapify a subtree rooted at index i, and heap_sort is the main sorting function.

The time complexity of Heap Sort is O(n log n), making it efficient for large datasets. It's important to note that Heap Sort has a consistent O(1) space complexity as it operates in-place.