class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        return (True if len(pattern) == len(words) and 
            len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)) 
            else False)
        