class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            res=-1
            for x in range(i+1):
                if x | x+1  == i:
                    res=x
                    break
            
            ans.append(res)
        return ans