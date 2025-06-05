class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)-1
        colnum = 0
        for x in columnTitle:
            # print(x)
            colnum = colnum + (ord(x)-ord('A')+1)*26**n
            n -= 1
        return colnum
