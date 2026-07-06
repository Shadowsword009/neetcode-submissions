class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0
        res = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
            elif nums1[l1] > nums2[l2]:
                res.append(nums2[l2])
                l2 += 1
            else:
                res.append(nums1[l1])
                res.append(nums2[l2])
                l1 += 1
                l2 += 1

        if l1 < len(nums1):
            res.extend(nums1[l1:])
        else:
            res.extend(nums2[l2:])
        mid = len(res) // 2

        if len(res) % 2 != 0:
            return res[mid]
        else:
            return (res[mid - 1] + res[mid]) / 2

        