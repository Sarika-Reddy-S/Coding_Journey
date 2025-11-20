class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1  # pointers for both strings
        carry = 0
        result = []

        # iterate from right to left
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))  # add binary bit
            carry = total // 2             # calculate carry

        # reverse and join result
        return ''.join(reversed(result))