class Solution(object):
    def isAnagram(self, s, t):
        if (''.join(sorted(s)))==(''.join(sorted(t))):
            return True
        return False