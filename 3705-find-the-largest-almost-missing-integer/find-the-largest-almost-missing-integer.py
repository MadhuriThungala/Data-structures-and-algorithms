class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        fm=defaultdict(int)
        for i in nums:
            fm[i]+=1
        uniq=[]
        for i,v in fm.items():
            if v==1:
                uniq.append(i)
        if k==1:
            return max(uniq) if uniq else -1
        first=nums[0] if fm[nums[0]]==1 else -1
        last=nums[-1] if fm[nums[-1]]==1 else -1
        return max(first,last)