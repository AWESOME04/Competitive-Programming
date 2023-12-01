"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        def dfs(emp_id):
            if not emp_map[emp_id].subordinates:
                return emp_map[emp_id].importance

            res = emp_map[emp_id].importance
            for sub_id in emp_map[emp_id].subordinates:
                res += dfs(sub_id)

            return res
            
        return dfs(id)        
