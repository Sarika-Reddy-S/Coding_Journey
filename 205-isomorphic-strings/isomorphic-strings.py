class Solution(object):
    def isIsomorphic(self, s, t):
        st={}
        ts={}
        for i in range(len(s)):
            if s[i] in st and st[s[i]]!=t[i]:
                return False
                break 
            if t[i] in ts and ts[t[i]]!=s[i]:
                return False
                break 
            st[s[i]]=t[i]
            ts[t[i]]=s[i]
        return True