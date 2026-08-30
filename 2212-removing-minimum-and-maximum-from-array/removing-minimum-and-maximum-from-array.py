class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini,maxi=nums.index(min(nums)),nums.index(max(nums))
        l,r=min(mini,maxi),max(mini,maxi)
        return min(r+1,n-l,l+1+n-r)
        