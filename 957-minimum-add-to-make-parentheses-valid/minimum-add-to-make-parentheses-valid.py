class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_par=0
        close=0
        for i in s:
            if i=="(":
                open_par+=1
            else:
                if open_par>0:
                    open_par-=1
                else:
                    close+=1
        return open_par+close