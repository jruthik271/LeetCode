class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        ans=float('inf')
        for i in range(len(a)):
            for j in range(len(c)):
                p=a[i]+b[i]
                r=max(p,c[j])
                s=r+d[j]

                x=c[j]+d[j]
                y=max(x,a[i])
                z=y+b[i]
                ans=min(ans,s,z)

        return ans
        