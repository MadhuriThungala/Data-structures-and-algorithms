class Solution:
    def maxDepth(self, s: str) -> int:
        d=0
        res=0
        for i in s:
            if i =="(":
                d-=1
            elif i==")":
                d+=1
            res=max(res,abs(d))
        return res