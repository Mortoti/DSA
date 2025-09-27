class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if s is made of a substring, it must appear in this    after         taking the first and last character
       return s in (s+s)[1:-1]
solution = Solution()
print(solution.repeatedSubstringPattern("abab"))
