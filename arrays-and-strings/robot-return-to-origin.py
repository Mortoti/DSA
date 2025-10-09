class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = r = u = d = 0
        for letter in moves:
            if letter == "L":
                l += 1
            elif letter == "R":
                r += 1
            elif letter == "U":
                u += 1
            elif letter == "D":
                d +=1
            else:
                pass
        return l == r and u == d
           

        
