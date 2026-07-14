class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        
        res=[]
        for i in range(1,len(mountain)-1):
            p=mountain[i-1]
            c=mountain[i]
            n=mountain[i+1]
            if p<c and c>n:
                res.append(i)
        
        return res