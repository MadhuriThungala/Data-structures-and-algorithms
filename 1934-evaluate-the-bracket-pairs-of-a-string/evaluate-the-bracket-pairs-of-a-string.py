class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp={}
        for k,v in knowledge:mp[k]=v
        start=False
        curr=[]
        res=[]
        for i in s:
            if i=="(":
                start=True
            elif i==")":
                start=False
                join="".join(curr)
                res.append(mp[join] if join in mp else "?")
                curr=[]
            else:
                if start:curr.append(i)
                else:res.append(i)
        return "".join(res)
        