class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        if not arr:
            return []

        a = set(arr)
        b = sorted(a)

        d = {}
        i = 1
        for x in b:
            d[x] = i
            i = i + 1

        res = []
        for x in arr:
            y = d[x]
            res.append(y)

        return res
