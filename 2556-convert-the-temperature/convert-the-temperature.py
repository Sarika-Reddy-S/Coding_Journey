class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        ans.append(float(f"{celsius+273.15:.5f}"))
        ans.append(float(f"{celsius* 1.80 + 32.00:.5f}"))
        return (ans)