class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign=-1 if x<0 else 1
        rev=0
        ma=2**31 - 1 
        mi=-(2**31)
        x=abs(x)
        while(x!=0):
            dig=x%10
            rev=rev*10+dig
            x//=10
        
        rev*=sign

        if rev>ma or rev<mi:
            return 0
        
        return rev