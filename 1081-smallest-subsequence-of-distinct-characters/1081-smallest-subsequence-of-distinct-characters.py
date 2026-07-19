class Solution:
    def smallestSubsequence(self, s: str) -> str:
        res=Counter(s)
        n=set()

        st=[]
         
        for c in s:
            res[c]-=1

            if c in n:
                continue

            while st and st[-1] > c and res[st[-1]]:
                n.remove(st.pop())
            
            st.append(c)
            n.add(c)

        return "".join(st)



