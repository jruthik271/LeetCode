class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi=float('inf')
        ar=[]
        re=[]
        for i in range(len(arr)-1):
            mi=min(mi,arr[i+1]-arr[i])
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==mi:
                re.append([arr[i],arr[i+1]])
        
        return re
