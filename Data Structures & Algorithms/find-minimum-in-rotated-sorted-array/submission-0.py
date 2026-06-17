class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n // 2

        l = 0
        r= n - 1
        while l<r:
            
            if nums[mid] > nums[r]:

                l = mid+1
                mid = (l+r) // 2
            else:
                r = mid
                mid = (l+r) // 2
        return nums[l]



        