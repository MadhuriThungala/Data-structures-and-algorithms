class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        reconstructed = [0] * k
        
        for b in range(30):
            count = 0
            for num in nums:
                if (num >> b) & 1:
                    count += 1
            
            for i in range(min(count, k)):
                reconstructed[i] |= (1 << b)
                
        total_sum = 0
        for num in reconstructed:
            total_sum = (total_sum + num * num) % MOD
            
        return total_sum