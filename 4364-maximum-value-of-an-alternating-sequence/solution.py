class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        # okay we need to write the maximum element 
        # two poss either increase by m or decrease by m so that any two of the conditions might hit , 
        # also keeping in mind it will start with s 


        # base thing is 
        if n==1:
            return s 

        # lets take one num and increase it (greedy way )

        num_middle = n//2
        x = s + num_middle * m -(num_middle-1)

        final_awnser_result = x
        return final_awnser_result
