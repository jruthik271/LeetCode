from typing import List
import math

class Solution:
    def firstRide(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        minTime = math.inf
        for i in range(len(ls)):
            minTime = min(minTime, ls[i] + ld[i])
        ans = math.inf
        for i in range(len(ws)):
            # if ws[i] < minTime: continue
            ans = min(ans, wd[i] + max(ws[i], minTime))
        return ans

    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        return min(self.firstRide(ls, ld, ws, wd), self.firstRide(ws, wd, ls, ld))