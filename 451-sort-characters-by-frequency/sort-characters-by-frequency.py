class Solution(object):
    def frequencySort(self, s):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=''
        for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
            ans += key * value
        return ans
                