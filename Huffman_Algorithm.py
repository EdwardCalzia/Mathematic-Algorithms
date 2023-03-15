from collections import Counter
import heapq

def huffman_encode(s):
    freq = Counter(s)
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huff_dict = dict(heapq.heappop(heap)[1:])
    encoded = ''.join(huff_dict[c] for c in s)
    return encoded, huff_dict

def huffman_decode(encoded, huff_dict):
    inv_huff_dict = {v: k for k, v in huff_dict.items()}
    decoded = ""
    code = ""
    for bit in encoded:
        code += bit
        if code in inv_huff_dict:
            decoded += inv_huff_dict[code]
            code = ""
    return decoded

s = "Hello, world!"
encoded, huff_dict = huffman_encode(s)
decoded = huffman_decode(encoded, huff_dict)
print("Original string:", s)
print("Huffman encoded string:", encoded)
print("Decoded string:", decoded)
