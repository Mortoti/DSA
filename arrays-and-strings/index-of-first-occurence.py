class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        length = len(needle) 
        if needle in haystack:
            for num in range(len(haystack)):
                if needle == haystack[num:num + length]:
                    result = num
                    break          
        return result
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))

