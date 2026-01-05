class Solution(object):
    def isBalanced(self, num):
        odd=[]
        evn=[]
        flag=False
        for i in range(len(num)):
            if i%2==0:
                odd.append(int(num[i]))
            else:
                evn.append(int(num[i]))
        if sum(odd)==sum(evn):
            flag=True
        return (flag)

