class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        for i in range(n):
            if n%(i+1)==0:
                summ+=nums[i]**2
        return summ
        