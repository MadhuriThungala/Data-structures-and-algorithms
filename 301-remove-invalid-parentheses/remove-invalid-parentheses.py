from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If we've found valid strings at this level, don't generate next level
            if found:
                continue

            # Generate all possible states by removing 1 parenthesis
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                
                next_state = curr[:i] + curr[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        return result