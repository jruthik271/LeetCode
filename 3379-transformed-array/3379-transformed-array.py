class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=nums.copy()
        for i in range(len(nums)):
            if nums[i]>0:
                j=(i+nums[i])%len(nums)
                res[i]=nums[j]
            elif nums[i]<0:
                j=(i+nums[i])%len(nums)
                res[i]=nums[j]
            elif nums[i]==0:
                res[i]=nums[i]
        
        return res