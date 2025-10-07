class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for op in operations:
            if op == "+":
                num = results[-1] + results[-2]
                results.append(num)
            elif op == "D":
                num = 2 * results[-1]
                results.append(num)
            elif op == "C":
                results.pop()
            else:
                num = int(op)
                results.append(num)
        return sum(results)
        
        
        
