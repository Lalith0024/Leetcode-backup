class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        binary = bin(n)[2:]
        string_binary = str(binary)
        compliment = ""
        for i in string_binary:
            if i == "1":
                compliment += "0"
            else:
                compliment += "1"
       
        return int(compliment,2)


