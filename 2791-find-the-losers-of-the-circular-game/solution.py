class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [0] * n
        count = 1
        pos = 0
        visited[pos] = 1
        while (visited[pos]!=2):
            pos = (pos+(count*k))%n
            visited[pos]+=1
            count+=1
        res = []
        for i in range(n):
            if not visited[i]:
                res.append(i+1)
        return res
        
