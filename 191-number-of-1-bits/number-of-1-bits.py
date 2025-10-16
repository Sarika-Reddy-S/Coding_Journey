class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=str(bin(n)[2:])
        c=0
        for i in ans[::-1]:
            if int(i)>0:
                c+=1
        return c