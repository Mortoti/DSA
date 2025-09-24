class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # XOR all chars in s and t, pairs cancel out, leaving the only extra char

        result = 0
        for letter in t + s:
                result ^= ord(letter)   
        return chr(result)

        
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))

        