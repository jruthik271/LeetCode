class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        # for i,j in Counter(nums).items():
        #     if j==n:
        #         return i

        ns=[i for i,j in Counter(nums).items() if j==n]
        res=ns[0]
        return res