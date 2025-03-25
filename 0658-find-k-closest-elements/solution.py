from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        xInd = self.binSearch(arr, x)
        
        leftPtr = xInd
        rightPtr = xInd + 1
        out = deque()

        for i in range(k):
            if leftPtr < 0:
                out.append(arr[rightPtr])
                rightPtr += 1
            elif rightPtr >= len(arr):
                out.appendleft(arr[leftPtr])
                leftPtr -= 1
            else:
                leftDist = abs(arr[leftPtr] - x)
                rightDist = abs(arr[rightPtr] - x)
                
                if leftDist <= rightDist:
                    out.appendleft(arr[leftPtr])
                    leftPtr -= 1
                else:
                    out.append(arr[rightPtr])
                    rightPtr += 1

        return list(out)

    # Find index where x would be in arr
    def binSearch(self, arr, x):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low - 1
