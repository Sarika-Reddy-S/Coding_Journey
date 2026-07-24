class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for i in operations:
            if (i).isnumeric() or i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i=='C':
                stack.pop()
            elif i=='D':
                val = int(stack[-1]) * 2
                stack.append(val)
            else:
                stack.append(int(stack[-2])+int(stack[-1]))
        return (sum(stack))
        