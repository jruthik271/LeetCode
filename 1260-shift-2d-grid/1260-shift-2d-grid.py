class Solution:
    def shiftGrid(self, a: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(a), len(a[0])
        ans = [row[:] for row in a]
        for i in range(n):
            for j in range(m):
                id = i * m + j + k
                r = (id // m) % n
                c = id % m
                ans[r][c] = a[i][j]
        return ans