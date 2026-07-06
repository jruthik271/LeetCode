class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        a,b,c=-1,-1,0
        
        for i,j in intervals:
            if i>a and j>b:
                a=i
                c+=1
            
            b=max(b,j)
        

        return c

        