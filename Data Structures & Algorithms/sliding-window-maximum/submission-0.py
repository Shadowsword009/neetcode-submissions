from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1

        curr = nums[l:r+1]
        res = []

        while r < len(nums):
            res.append(max(curr))

            r += 1
            if r < len(nums):
                curr.append(nums[r])
                curr.pop(0)

        return res