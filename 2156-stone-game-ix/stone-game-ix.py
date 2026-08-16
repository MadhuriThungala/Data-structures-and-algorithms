class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        ct0=ct1=ct2=0
        for i in stones:
            if(typ:=i%3)==0:
                ct0+=1
            elif typ==1:
                ct1+=1
            else:
                ct2+=1
        if ct0%2==0:
            return ct1>=1 and ct2>=1
        return ct1-ct2>2 or ct2-ct1>2