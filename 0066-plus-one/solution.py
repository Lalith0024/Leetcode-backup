class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # so array length can be 1-100 okay 
        # so basically focus on untis pace 9 -> 10
        # what if  0 is in units place? 
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])
        ans = int(string) + 1
        converted_str = str(ans)
        arr = []
        for i in converted_str:
            arr.append(int(i))
        return arr
