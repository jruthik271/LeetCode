class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """

        res=[]
        for i in s:
            if i.islower():
                res.append(i)
            elif i=="#":
                res*=2
            elif i=="*":
                if res:
                    res.pop()
            elif i=="%":
                res.reverse()
            
        return "".join(res)
        