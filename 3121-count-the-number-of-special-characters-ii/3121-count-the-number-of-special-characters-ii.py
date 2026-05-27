class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):

            if ch.islower():
                lower_last[ch] = i

            else:
                if ch not in upper_first:
                    upper_first[ch] = i

        count = 0

        for ch in lower_last:

            upper = ch.upper()

            if upper in upper_first:

                if lower_last[ch] < upper_first[upper]:
                    count += 1

        return count