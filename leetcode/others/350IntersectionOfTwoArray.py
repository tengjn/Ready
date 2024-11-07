class Solution(object):
    def intersection(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        out = []
        if len1 < len2:
            temp = nums1
            nums1 = nums2
            nums2 = temp
        for item in nums1:
            if item in nums2:
                nums2[nums2.index(item)] = -1
                print(nums2)
                out.append(item)
        return out

cls = Solution()
output = cls.intersection([3, 1, 2], [1, 1])
print(output)