class Solution(object):
    def reverseWords(self, s):
        s1=s.split(" ")
        ans=''
        for i in range(len(s1)):
            ans+=(s1[i][::-1])
            if len(s1)-1==i:
                ans+=""
            else:
                ans+=' '
        return(ans)
                