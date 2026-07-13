class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
        dig="123456789"
        res=[]
        for i in range(2,10):
            for j in range(10-i):
                ans=int(dig[j:j+i])
                if low<=ans<=high:
                    res.append(ans)
        
        return res