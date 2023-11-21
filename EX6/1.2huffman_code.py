import heapq
from collections import defaultdict

def build_huffman_tree(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]

# Example usage:
text = "abracadabra"
frequency = defaultdict(int)
for char in text:
    frequency[char] += 1

huffman_tree = build_huffman_tree(frequency)
print("Huffman Codes:")
for char, code in huffman_tree:
    print(f"{char}: {code}")
