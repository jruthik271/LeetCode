class Solution:
    def pro(self,n):
        n=abs(n)
        r=1
        if n==0:
            return 0
        while(n>0):
            dig=n%10
            r*=dig
            n//=10
        return r
    def smallestNumber(self, n: int, t: int) -> int:
        
        
        while True:
            if self.pro(n)%t==0:
                return n
            n+=1
            
        
    