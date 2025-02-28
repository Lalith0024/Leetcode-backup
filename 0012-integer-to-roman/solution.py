class Solution(object):
    def intToRoman(self, num):
        roman_numbers = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        def rec(num,roman_numbers):
            if num==0:
                return ""
            for val,symbol in roman_numbers:
                if num>=val:
                    return symbol + rec(num-val,roman_numbers)
            return ""
        return(rec(num,roman_numbers))


        
