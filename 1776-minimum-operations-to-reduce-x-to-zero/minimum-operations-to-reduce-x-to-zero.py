class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:
            return len(nums)
        if target<0:
            return -1
        left=0
        curr_sum=0
        max_len=-1
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum>target and left<=r:
                curr_sum-=nums[left]
                left+=1
            if curr_sum==target:
                max_len=max(max_len,r-left+1)
        return len(nums)-max_len if max_len!=-1 else -1