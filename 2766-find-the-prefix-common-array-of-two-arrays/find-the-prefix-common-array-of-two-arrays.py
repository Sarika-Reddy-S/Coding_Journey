class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        i=len(A)
        val=[]
        while i!=0:
            temp=0
            for b in B[:i]:
                temp+=(A[:i].count(b))
            val.append(temp)
            i-=1
        return (val[::-1])