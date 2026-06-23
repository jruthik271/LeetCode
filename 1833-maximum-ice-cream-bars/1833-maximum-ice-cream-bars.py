class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        c=0
        
        costs.sort()
        for i in costs:
            if i>coins:
                break
            
            c+=1
            coins-=i

        return c

            
