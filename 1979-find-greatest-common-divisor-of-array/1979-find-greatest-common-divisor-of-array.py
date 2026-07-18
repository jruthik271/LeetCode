class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma=max(nums)
        mi=min(nums)

        return gcd(ma,mi)