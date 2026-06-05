class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res=float('inf')
        n=len(words)
        for i in range(n):
            if words[i]==target:
                d=abs(i-startIndex)
                res=min(res,min(d,n-d))
        
        if res!=float('inf'):
            return res
        else:
            return -1

       