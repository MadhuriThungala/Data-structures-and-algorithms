class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def dp(i,seg,first):
            if seg==0:
                return 1
            if i==n:
                return 0
            res=dp(i+1,seg,first)
            if first:res+=dp(i+1,seg,False)
            else:res+=dp(i,seg-1,True)
            return res%(10**9+7)
        return dp(0,k,True)
        