class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        st = set()
        for x, y in obstacles:
            st.add((x, y))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        x,y = 0,0
        ans = 0
        d = 0

        # north -> +Y direction 
        # south -> -Y direction 
        # east -> +X direction 
        # West -> -X direction 

        # just execute the distance without obstacles first 

        for i in commands:
            if i==-1:
                d = (d+1)%4
            elif i==-2:
                d = (d+3)%4
            
            else:
                for j in range(i):
                    tempx = x + directions[d][0]
                    tempy = y + directions[d][1]
                    if (tempx,tempy) in st:
                        break
                    x,y = tempx,tempy
                    ans = max(ans,x*x + y*y)

        return ans






            



