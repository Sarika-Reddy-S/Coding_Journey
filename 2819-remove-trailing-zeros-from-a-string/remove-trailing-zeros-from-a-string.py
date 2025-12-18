class Solution(object):
    def removeTrailingZeros(self, num):
        ans = list(num)
        n = len(ans) - 1
        val = ''

        # remove trailing zeros
        while n >= 0 and ans[n] == '0':
            n -= 1

        # build reversed value
        while n >= 0:
            val += ans[n]
            n -= 1

        return val[::-1]