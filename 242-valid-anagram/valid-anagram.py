class Solution(object):
    def isAnagram(self, s, t):
        lst1=[]
        lst2=[]
        for i in s:
            lst1.append(ord(i))
        for i in t:
            lst2.append(ord(i))
        if sorted(lst1)==sorted(lst2):
            return True
        else:
            return False