class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        res=abs(30*hour - 5.5*minutes)
        if res>180:
            return 360-res
        
        return res