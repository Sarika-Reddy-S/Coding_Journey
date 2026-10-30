class Solution(object):
    def findPeaks(self, mountain):
        lst=[]
        for i in range(1,len(mountain)-1):
            if mountain[i]>mountain[i-1] and mountain[i+1]<mountain[i]:
                lst.append(i)
        return lst