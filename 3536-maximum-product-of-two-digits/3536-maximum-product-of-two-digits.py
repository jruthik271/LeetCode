class Solution:
    def maxProduct(self, n: int) -> int:
        a=0
        b=0
        while n>0:
            x= n%10
            if x>a:
                a,b=x,a
            elif x>b:
                b=x
            n//=10 
        return a*b