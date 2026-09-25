class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res, cur = set(), [{""}]
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isalpha():
                j = i
                while j < len(expression) and expression[j].isalpha():
                    j += 1
                word = expression[i:j]
                i = j - 1
                
                cur[-1] = {a + b for a in cur[-1] for b in {word}}
                
            elif char == '{':
                stack.append((res, cur))
                res, cur = set(), [{""}]
                
            elif char == '}':
                completed_set = res.union(*cur)
                res, cur = stack.pop()
                cur[-1] = {a + b for a in cur[-1] for b in completed_set}
                
            elif char == ',':
                res.update(*cur)
                cur = [{""}]
                
            i += 1
            
       
        return sorted(list(res.union(*cur)))
        