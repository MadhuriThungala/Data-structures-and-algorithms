from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        vector_counts = Counter()
        
        for r1, c1 in list1:
            for r2, c2 in list2:
                dr = r2 - r1
                dc = c2 - c1
                vector_counts[(dr, dc)] += 1
                
        
        return max(vector_counts.values()) if vector_counts else 0