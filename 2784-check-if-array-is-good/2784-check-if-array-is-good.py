class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        res=list(range(1,n)) + [n-1]
        return nums==res
