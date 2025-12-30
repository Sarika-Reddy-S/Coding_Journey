class Solution:
    def moveZeroes(self, nums):
        pos = 0
        
        # Move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        # Fill remaining positions with zero
        for i in range(pos, len(nums)):
            nums[i] = 0
