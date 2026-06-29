class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for s in patterns:
            if s in word:
                c+=1
            
        return c