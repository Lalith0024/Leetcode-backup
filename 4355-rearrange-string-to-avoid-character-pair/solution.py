class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # brute force is take all the permutaiotns and check the satisfing conditions and return it , 

        # but yeah we could solve it rearraging by changing char to s , and take a basic function whcich returns some identification , and we will automatically check them 

        char = s

        def weight(char_element):
            if char_element == y:
                return 0
            if char_element == x:
                return 2 
            return 1

        pre_res = sorted(list(char),key = weight)
        final_res = "".join(pre_res)

        return final_res
            
