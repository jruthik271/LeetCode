class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p=0
        n=len(nums)
        while p < n-2 and nums[p]<nums[p+1]:
            p+=1
        
        if p==0:
            return False
        q=p
        while q<n-1 and nums[q]>nums[q+1]:
            q+=1
        if p==q or q==n-1:
            return False
        while q<n-1 and nums[q]<nums[q+1]:
            q+=1

        return q==n-1
        