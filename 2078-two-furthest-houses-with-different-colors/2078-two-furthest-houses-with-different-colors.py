class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n=len(colors)
        diff=0
        for i in range(n):
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                    diff=max(diff,j-i)
                    
        return diff