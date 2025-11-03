class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = 0
        substring = ""

        for ch in s:
            if ch in substring:
                # cut substring from first duplicate occurrence
                substring = substring[substring.index(ch)+1:]
            substring += ch
            count = max(count, len(substring))
        return count

        