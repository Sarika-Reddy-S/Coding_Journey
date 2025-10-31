import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        # Calculate logarithm base 3
        ans = math.log(n, 3)
        # Check if ans is (almost) an integer
        return abs(round(ans) - ans) < 1e-10
