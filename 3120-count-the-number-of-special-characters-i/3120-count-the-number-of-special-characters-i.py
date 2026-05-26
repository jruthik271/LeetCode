class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower_ = set()
        upper_ = set()
        for ch in word:
            if ch.islower():
                lower_.add(ch)
            else:
                upper_.add(ch.lower())

            
        return len(lower_ & upper_)
        
        