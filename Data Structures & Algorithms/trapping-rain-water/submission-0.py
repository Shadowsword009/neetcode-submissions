class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        l,r = 0, len(height) - 1
        mr = height[r]
        ml = height[l]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                ml = max(ml,height[l])
                res += ml - height[l]
            else:
                r -= 1
                mr = max(mr,height[r])
                res += mr - height[r]
        return res