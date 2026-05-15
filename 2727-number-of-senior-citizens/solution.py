class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for i in details:
            arr = []
            for s in i:
                arr.append(s)
            
            age = (arr[11:13])
            numer = "".join(age)
            if int(numer)>60:
                c+=1
        return c
