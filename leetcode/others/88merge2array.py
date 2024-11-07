# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p, q, k = m - 1, n - 1, len(nums1) - 1
        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[k] = nums1[p]
                p -= 1
            else:
                nums1[k] = nums2[q]
                q -= 1
            k -= 1

        while q >= 0:
            nums1[k] = nums2[q]
            k -= 1
            q -= 1


# idx = 0
# while(idx < total_len):
#     if (not len(a) == 0) and (not len(b) == 0):
#         if a[0] < b[0]:
#             c[idx] = a[0]
#             a.pop(0)
#         else:
#             c[idx] = b[0]
#             b.pop(0)
#     elif len(a) == 0:
#         c[idx] = b[0]
#         b.pop(0)
#     elif len(a) == 0:
#         c[idx] = a[0]
#         a.pop(0)
#     idx += 1

