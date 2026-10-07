class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        number = []
        for word in words:
            val=0
            for w in word:
                val+=(weights[ord(w.upper()) - ord('A')])
            number.append(val%26)
        print(number)
        ans=[]
        for ch in number:
            ans.append(chr(ord('z') - ch))
        return ''.join(ans)