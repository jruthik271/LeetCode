class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        pgcd=[]

        mx=0

        for i in range(n):
            mx=max(nums[i],mx)
            a=math.gcd(nums[i],mx)
            pgcd.append(a)

        pgcd.sort()

        ans=0
        for i in range(n//2):
            ans+= math.gcd(pgcd[i],pgcd[n-i-1])
        
        return ans