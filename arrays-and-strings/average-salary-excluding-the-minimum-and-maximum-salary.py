class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = max_salary = salary[0]
        total = 0
        for num in salary:
            if num < min_salary:
                min_salary = num
            elif num > max_salary:
                max_salary = num
            else:
                pass
            total += num
        return (total-(max_salary + min_salary) )/ (len(salary) - 2)
