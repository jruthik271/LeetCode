class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        c=nums[0]
        m=float('inf')
        n=float('inf')
        for i in nums[1:]:
            if i<m:
                n=m
                m=i
            elif i<n: 
                n=i

        return c+m+n
        