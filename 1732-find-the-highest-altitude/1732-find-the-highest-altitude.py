class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=0
        ma=a
        for i in gain:
            a+=i
            ma=max(ma,a)
        
        return ma

        