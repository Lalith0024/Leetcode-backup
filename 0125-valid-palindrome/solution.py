class Solution:
    def isPalindrome(self, s: str) -> bool:
       

        s = s.lower()


        filtered_string = ""

        for i in s:
        
            if i.isalpha() or i.isdigit():
                filtered_string += i

        if filtered_string == filtered_string[::-1]:
            return True
        return False

            
