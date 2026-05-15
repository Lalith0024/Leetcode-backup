class Solution:
    def asteroidsDestroyed(self, mass: int, arr: List[int]) -> bool:
        arr.sort()
        for k in arr:
            if mass>=k:
                mass+=k
            else:
                return False
        return True
            
