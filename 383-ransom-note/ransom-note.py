class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        have = Counter(magazine)
        # For every character needed in ransomNote
        for ch, cnt in need.items():
            if have[ch] < cnt:
                return False
        return True