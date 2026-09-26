class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans=[]
        left = 0
        right = 0

        while left <len(word1) or right<len(word2):
            if len(word1)!=left:
                ans.append(word1[left])
                left += 1
            if len(word2)!=right:
                ans.append(word2[right])
                right += 1
        return ''.join(ans)
        