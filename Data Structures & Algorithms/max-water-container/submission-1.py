class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxa = 0
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            maxa =    max(area,maxa)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
        return maxa