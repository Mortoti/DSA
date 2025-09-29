class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        initial = ""
        for letter in digits:
            initial += str(letter)
        main = int(initial) + 1
        for num in str(main):
            result.append(int(num))
        return result
