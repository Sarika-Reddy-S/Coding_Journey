import itertools
class Solution(object):
    def validStrings(self, n):
        combinations = itertools.product(['0', '1'], repeat=n)
        result =[]
        for i in combinations:
            val=''.join(i)
            if '00' not in val:
                result.append(val)
        return result