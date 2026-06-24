class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        s=Counter(moves)
        r=s['R']
        l=s['L']
        u=s['U']
        d=s['D']
        return r==l and u==d