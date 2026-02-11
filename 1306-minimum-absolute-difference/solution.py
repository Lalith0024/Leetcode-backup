class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        l=[]
        minm=float('inf')
        for i in range(1,len(arr)):
            minm=min(minm,arr[i]-arr[i-1])
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==minm:
                ans.append([arr[i-1],arr[i]])
        return ans


