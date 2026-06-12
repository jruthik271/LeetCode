class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n=len(letters)
        l=0
        r=n-1
        if target>=letters[r]:
            return letters[l]
        

        while(l<=r):
            mid=(l+r)//2

            if letters[mid]>target:
                r=mid-1
            else:
                l=mid+1
            
        return letters[l]