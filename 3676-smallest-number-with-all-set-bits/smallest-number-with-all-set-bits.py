class Solution(object):
    def smallestNumber(self, n):
        a = str(bin(n)[2:])        
        c = sum(int(i) for i in a) 
        ans = a.replace('0', '1')  
        a_sum = sum(int(i) for i in ans)  
        num_from_ans = int(ans, 2)
        if a_sum >= c:
            return (num_from_ans)
        else:
            return (a_sum)
        