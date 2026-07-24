class Solution(object):
    def backspaceCompare(self, s, t):
        lst=[]
        for i in s:
            if i!='#':
                lst.append(i)
            else:
                del lst[-1:]
        lst1=[]
        for i in t:
            if i!='#':
                lst1.append(i)
            else:
                del lst1[-1:]
        if lst1==lst:
            return True
        else:
            return False