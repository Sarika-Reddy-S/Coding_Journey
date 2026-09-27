class Solution(object):
    def isPalindrome(self, s):
        st=(''.join(ch.lower() for ch in s if ch.isalnum()))
        return st == st[::-1]