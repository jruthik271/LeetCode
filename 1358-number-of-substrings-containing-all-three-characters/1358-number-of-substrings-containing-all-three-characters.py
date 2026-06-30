class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ch={'a':-1,'b':-1,'c':-1}

        count=0

        for i,j in enumerate(s):
            ch[j]=i
            count+=min(ch['a'],ch['b'],ch['c'])+1
        
        return count