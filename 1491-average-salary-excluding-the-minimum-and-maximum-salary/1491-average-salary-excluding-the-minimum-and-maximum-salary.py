class Solution:
    def average(self, salary: List[int]) -> float:
        #removing max and min salary
        salary.remove(max(salary))
        salary.remove(min(salary))
        #calculating the average salary
        return sum(salary)/len(salary)
        