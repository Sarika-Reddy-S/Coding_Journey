class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        number = []
        for word in words:
            val=0
            for w in word:
                val+=(weights[ord(w.upper()) - ord('A')])
            number.append((chr(ord('z') - (val%26))))
        return ''.join(number)