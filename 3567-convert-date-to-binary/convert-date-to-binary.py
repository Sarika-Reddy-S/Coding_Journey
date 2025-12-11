class Solution:
    def convertDateToBinary(self, date: str) -> str:
        vals = date.split('-')
        ans=[]
        for i in vals:
            ans.append(bin(int(i))[2:])
        return ('-'.join(ans))