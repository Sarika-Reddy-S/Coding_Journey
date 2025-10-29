class Solution(object):
    def plusOne(self, digits):
        ans=''
        a=[]
        for d in digits:
            ans+=str(d)
        half=str(int(ans)+1)
        for i in half:
            a.append(int(i))
        return (a)
        