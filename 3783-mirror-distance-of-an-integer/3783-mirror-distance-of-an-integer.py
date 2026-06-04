class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=int(str(n)[::-1])
        di=abs(n-rev)
        return di