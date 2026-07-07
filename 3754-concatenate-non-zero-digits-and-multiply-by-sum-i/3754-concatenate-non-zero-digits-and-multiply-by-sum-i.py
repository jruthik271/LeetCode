class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits=[int(i) for i in str(n) if i!="0"]

        if not digits:
            return 0

        su=sum(digits) 
        num=int("".join(map(str, digits)))
        return num*su