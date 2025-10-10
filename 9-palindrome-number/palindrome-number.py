class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        d=(a[::-1])
        if a[:]==d:
            return True
        else:
            return False