class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete, one_delete, best = arr[0], arr[0], arr[0]
        for i in range(1, len(arr)):
            one_delete = max(no_delete, one_delete + arr[i])
            no_delete = max(arr[i], no_delete + arr[i])
            best = max(no_delete, one_delete, best)
        return best  
        
