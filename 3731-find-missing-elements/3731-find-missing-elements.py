class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        mx=max(nums)
        nums.sort()
        res=[]
        for i in range(m,mx):
            if i not in nums:
                res.append(i)
                
        return res