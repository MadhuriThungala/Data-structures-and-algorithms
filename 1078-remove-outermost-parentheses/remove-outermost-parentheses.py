class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        balance = 0

        for ch in s:
            if ch == '(':
                if balance:
                    ans.append(ch)
                balance += 1
            else:
                balance -= 1
                if balance:
                    ans.append(ch)

        return ''.join(ans)