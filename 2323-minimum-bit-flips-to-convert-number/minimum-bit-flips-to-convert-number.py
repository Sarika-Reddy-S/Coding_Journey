class Solution(object):
    def minBitFlips(self, start, goal):
        val=(bin(start^goal)[2:])
        c=0
        for i in val:
            if i=='1':
                c+=1
        return c