class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)

        sum_salaries = sum(salary) - min_salary - max_salary

        num_salaries = len(salary) - 2
        average_salary = sum_salaries / num_salaries

        return average_salary
