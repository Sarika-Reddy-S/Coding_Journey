class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        lst = []
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            ans = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans = nums2[j]
                    break
            lst.append(ans)
        return lst