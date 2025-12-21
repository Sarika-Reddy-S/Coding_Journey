import re
class Solution(object):
    def checkRecord(self, s):
        if s.count('A') >= 2:
            return False
        
        # Condition 2: no 3 consecutive L
        if 'LLL' in s:
            return False
        
        return True