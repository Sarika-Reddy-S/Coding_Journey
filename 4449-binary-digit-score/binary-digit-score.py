class Solution(object):
    def calculateScore(self, a, b):
        count_a=(bin(a)[2:]).count('1')
        count_b=(bin(b)[2:]).count('1')
        if count_a>=count_b:
            return count_a*count_b
        return count_b/count_a