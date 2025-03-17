class Solution:
    def validStrings(self, n: int) -> List[str]:
        total_strings = 2**n
        valid_strings = []
        
        for num in range(total_strings):
            binary_str = ""
            temp_num = num  
            
            while temp_num > 0:
                remainder = temp_num % 2
                binary_str = str(remainder) + binary_str
                temp_num = temp_num // 2
            
            while len(binary_str) < n:
                binary_str = "0" + binary_str
            
            if "00" not in binary_str:
                valid_strings.append(binary_str)
        
        return valid_strings

        
