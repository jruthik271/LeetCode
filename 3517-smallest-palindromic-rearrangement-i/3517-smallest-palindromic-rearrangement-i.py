class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # c=list(s)
        # n=len(c)
        # c.sort()
        # # return c
        # for i in range(len(s)):
        #     if c[i]==c[i+1]:

        # return "".join(c)
        freq=Counter(s)
        left=""
        mid=""

        for ch in sorted(freq):
            left+= ch * (freq[ch]//2)

            if freq[ch]%2==1:
                mid=ch

        return left+mid+left[::-1]