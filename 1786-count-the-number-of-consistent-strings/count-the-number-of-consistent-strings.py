class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for w in words:
            if all(car in allowed for car in w ):
                c+=1
        return c