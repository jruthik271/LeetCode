class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # arr=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         arr.append(max(nums[i:j+1])-min(nums[i:j+1]))
        
        # re=max(arr)

        # return re*k
        return (max(nums)-min(nums))*k