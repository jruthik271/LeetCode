class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        eve=n*(n+1)
        odd=n*n
        return math.gcd(eve,odd)