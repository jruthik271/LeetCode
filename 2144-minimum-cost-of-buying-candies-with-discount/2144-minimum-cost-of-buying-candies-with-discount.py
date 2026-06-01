class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        c=0
        for i in range(len(cost)):
            if i%3==2:
                c+=cost[i]
        
        return sum(cost)-c