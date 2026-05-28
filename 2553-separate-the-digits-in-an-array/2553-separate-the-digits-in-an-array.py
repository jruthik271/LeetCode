class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s=[]
        for i in range(len(nums)):
            temp=[]
            while nums[i]!=0:
                n=nums[i]%10
                temp.append(n)
                nums[i]//=10
                
            temp.reverse()
            s.extend(temp)
        
        return s