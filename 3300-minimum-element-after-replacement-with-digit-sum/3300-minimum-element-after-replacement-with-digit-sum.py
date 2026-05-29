class Solution:
    def minElement(self, nums: List[int]) -> int:
        s=[]
        for i in range(len(nums)):
            temp=[]
            c=0
            while nums[i]!=0:
                n=nums[i]%10
                c+=n
                nums[i]//=10
            temp.append(c)
            s.extend(temp)
        
        return min(s)
