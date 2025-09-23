class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        word = ""
        if len1 == len2:
            for letter in range(len1):
                 word+=word1[letter]
                 word+=word2[letter]
        elif len1 > len2:
            length = len2
            for letter in range(length):
                word+=word1[letter]
                word+=word2[letter]
            word+=word1[letter+1::]
        else:
            length = len1
            for letter in range(length):
                word+=word1[letter]
                word+=word2[letter]
            word+=word2[letter+1::]
        return word
solution =Solution()
print(solution.mergeAlternately("abc", "pqr"))
            
