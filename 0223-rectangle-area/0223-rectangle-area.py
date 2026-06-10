class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        area1=(ax2-ax1)*(ay2-ay1)
        area2=(bx2-bx1)*(by2-by1)

        tot=area1+area2

        overlap_wid=min(ax2,bx2)-max(ax1,bx1)
        overlap_hie=min(ay2,by2)-max(ay1,by1)
        
        com=0
        if overlap_wid>0 and overlap_hie>0:
            com=overlap_wid*overlap_hie
        
        return tot-com
        
