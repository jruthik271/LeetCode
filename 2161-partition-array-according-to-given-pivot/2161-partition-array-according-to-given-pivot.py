class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        s=[]
        for i in range(len(nums)):
            if nums[i]==pivot:
                s.append(nums[i])
            elif nums[i]<pivot:
                l.append(nums[i])
            else:
                r.append(nums[i])
        
        return l+s+r