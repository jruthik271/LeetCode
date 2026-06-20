class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        x=0
        y=0

        for i in nums1:
            if i in nums2:
                x+=1
        
        for j in nums2:
            if j in nums1:
                y+=1

        s=[]
        s.append(x)
        s.append(y)
        return s