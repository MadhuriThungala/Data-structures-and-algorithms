from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
               
                reserved[row] |= (1 << (seat - 2))
        
        max_groups = n * 2
        
       
        left_mask = 15    
        middle_mask = 60   
        right_mask = 240   
        
        
        for mask in reserved.values():
            can_left = (mask & left_mask) == 0
            can_right = (mask & right_mask) == 0
            can_middle = (mask & middle_mask) == 0
            
            if can_left and can_right:
                continue  
            elif can_left or can_right or can_middle:
                max_groups -= 1 
            else:
                max_groups -= 2 
                
        return max_groups
        