class Solution(object):
    def findThePrefixCommonArray(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        a_visited=set()
        b_visited=set()

        count=0
        c=[]

        for i in range(len(a)):

            if a[i] in b_visited:
                count+=1

            if b[i] in a_visited:
                count+=1

            if a[i]==b[i]:
                count+=1

            a_visited.add(a[i])
            b_visited.add(b[i])

            c.append(count)

        
        return c