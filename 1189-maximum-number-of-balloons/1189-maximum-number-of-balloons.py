class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s=Counter(text)
        b=s['b']
        a=s['a']
        l=s['l']//2
        o=s['o']//2
        n=s['n']
        mi=min(b,a,l,o,n)
        return mi
