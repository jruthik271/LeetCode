class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        ans = numBottles

        while numBottles >= numExchange:

            new = numBottles // numExchange
            rem = numBottles % numExchange

            ans += new
            numBottles = new + rem

        return ans