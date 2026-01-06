class Solution(object):
    def isBalanced(self, num):
        odd=[]
        evn=[]
        for i in range(len(num)):
            if i%2==0:
                odd.append(int(num[i]))
            else:
                evn.append(int(num[i]))
        return (sum(evn)==sum(odd))

