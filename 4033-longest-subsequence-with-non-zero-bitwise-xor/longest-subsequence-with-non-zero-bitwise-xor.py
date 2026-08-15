class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        totalXor=0
        allzeros=True
        for x in nums:
            totalXor^=x
            if x>0:
                allzeros=False
        if totalXor>0:
            return n
        return n-1 if allzeros==False else 0