class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_dict = {i: chr(123 - i) for i in range(1, 27)}  # z=1, y=2 ... a=26
        arr=[]
        ans=[]
        for ch in s:
            for num, alpha in reverse_dict.items():
                if ch == alpha:
                    arr.append(num)
        for i in range(0,len(s)):
            a=i+1
            ans.append(arr[i]*a)
        return (sum(ans))