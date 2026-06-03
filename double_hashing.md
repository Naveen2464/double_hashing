# Double Hashing

## Overview
Double Hashing is a collision resolution technique used in Open Addressing hash tables. It uses two different hash functions to calculate the interval between probes.

## How it Works
When a collision occurs at index `h1(key)`, we calculate a jump size using `h2(key)`. The sequence of probes is:
$index = (h1(key) + i \cdot h2(key)) \pmod{size}$
where $i = 0, 1, 2, ...$

1.  **Primary Hash ($h_1$):** Determines the initial bucket.
2.  **Secondary Hash ($h_2$):** Determines the "step size". 
    *   **Crucial:** $h_2(key)$ must never result in 0, otherwise the probe will loop on the same index.
    *   Ideally, $h_2(key)$ should be relatively prime to the table size.

## Advantages
*   **Eliminates Clustering:** Unlike Linear Probing (which causes primary clustering) or Quadratic Probing (secondary clustering), double hashing provides a probe sequence that depends on the key in two ways, spreading keys more uniformly.

## Complexity
*   **Average Case:** $O(1)$ for Insert, Search, and Delete.
*   **Worst Case:** $O(size)$ if the table is nearly full or the hash functions are poor.
