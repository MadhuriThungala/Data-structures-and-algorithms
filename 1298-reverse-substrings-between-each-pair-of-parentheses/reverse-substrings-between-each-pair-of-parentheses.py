class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i ==")":
                curr=[]
                while stack and stack[-1]!="(":
                    curr.append(stack.pop())
                stack.pop()
                stack+=curr
            else:
                stack.append(i)
        return "".join(stack)

        