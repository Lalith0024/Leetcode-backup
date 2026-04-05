class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # we are given -> robot starts at (0,0) the origin on a 2D plane 
        # so count of L == R and U == D -> reach at origin? you sure? lets take a case and check L , D , D, R, U, U yes! works lets go with that approach 

        # in python .count()?


        if((moves.count("L")==moves.count("R")) and (moves.count("U")==moves.count("D"))):
            return True
        else:
            return False

        # .count()-> takes 0(n) -> o(n)+ o(n)+ o(n) + o(n) -> o(4n) which results in o(n) solution 
        # can we optimize it? -> i guess no without traversing entire string its impossible to determine if the person can reach back .. 
        
