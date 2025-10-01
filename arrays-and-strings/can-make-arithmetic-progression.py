class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        number = arr
        difference = number[1]- number[0]
        for num in range(len(number)-1):
            if number[num+1]-number[num] != difference:
                return False
        return True
            
        
