class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        num = 0
        prev = 0
        for letter in reversed(s):
            number = dictionary[letter]
            if number < prev:
                num -= number
               
            else:
                num += number
            prev = number
                
        return num
