class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0 :
            return int((high-low)/2 + 1)
        elif high % 2 != 0:
            return int((high-low)/2) + 1
        else:
            return int((high-low)/2)
