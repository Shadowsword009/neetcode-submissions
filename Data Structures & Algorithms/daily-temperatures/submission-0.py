class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            j = 1

            while i + j < len(temperatures) and temperatures[i+j] <= temperatures[i]:
                j += 1

            if i + j < len(temperatures):
                res.append(j)
            else:
                res.append(0)

        return res