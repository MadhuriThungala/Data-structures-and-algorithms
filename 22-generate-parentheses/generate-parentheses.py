class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def backtrack(open_count:int,close_count:int,curr_str:int):
            if len(curr_str)==2*n:
                res.append(curr_str)
                return
            if open_count<n:
                backtrack(open_count+1,close_count,curr_str+"(")
            if close_count<open_count:
                backtrack(open_count,close_count+1,curr_str+")")
        backtrack(0,0,"")
        return res
        