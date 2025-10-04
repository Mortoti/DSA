class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word1 = s.split()
        word = word1.pop()
        return len(word) 
