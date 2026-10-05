class Solution:
    def checkValidString(self, s: str) -> bool:
        blc=0
        for i in s:
            if i=="(" or i=="*":
                blc+=1
            else:
                blc-=1
            if blc<0:
                return False
        blc=0
        for j in reversed(s):
            if j==")" or j=="*":
                blc+=1
            else:
                blc-=1
            if blc<0:
                return False
        return True

