class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxa = 0
        curr = 0
        while l<r:
            curr = min(heights[l],heights[r])* (r-l)
            maxa = max(maxa,curr) 
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        return maxa
            
        