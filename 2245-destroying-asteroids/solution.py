class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # we should think in a greedy way like to pick the most optimal for our solution such that nothing breaks down 
        asteroids.sort()
        # first pick 
        for i in range(len(asteroids)):
            if asteroids[i]<=mass:
                mass += asteroids[i]
            else:
                return False 
        return True

        

        # you have picked first but we should not think like picking first or second 

