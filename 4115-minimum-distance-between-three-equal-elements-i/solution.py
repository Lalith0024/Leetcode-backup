class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # perfect tupple -> (i,j,k) -> arr[i] == arr[j] == arr[k]
        # Note - > i<j<k
        # abs(i-j) + abs(j-k) + abs(k-i) = 2*(k-i)

        n = len(nums)
        # edge case 
        if n <= 2:
            return -1
        ans = float('inf')

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    # if match hunt for k , and update ans -> you could use the abs and stuff but more additive operations would happen there.. 
                    
                    for k in range(j+1, n):
                        if nums[j] == nums[k]:
                            ans = min(ans, 2*(k-i))
        return -1 if ans == float('inf') else ans
