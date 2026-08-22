import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits=[int(i) for i in str(n)]
        total=sum(digits)+math.prod(digits)
        return n%total==0

        