class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[]
        sums=[]
        for i in s:
            a.append(ord(i))
        for j in range(len(a)-1):
            sums.append(abs(a[j]-a[j+1]))
        return (sum(sums))