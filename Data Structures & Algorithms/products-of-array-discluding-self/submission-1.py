class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            ele = 1
            for j in range (len(nums)):

                if j == i:
                    continue
                else:
                    ele *= nums[j]
            res.append(ele)
        return res
