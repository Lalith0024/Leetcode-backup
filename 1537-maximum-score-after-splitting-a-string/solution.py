class Solution:
    def maxScore(self, s: str) -> int:
        arr = [int(digit) for digit in s] #all numbers
        c = 0
        cont_0=[0]*len(arr) #count of 0
        for i in range(len(arr)-1):
            if arr[i] == 0:
                c+=1
                cont_0[i]=(c) #dry run this
            else:
                cont_0[i]=(c)
        pref = [0]*len(arr)
        pref[0] = arr[0]
        for i in range(1,len(arr)):
            pref[i] = (pref[i-1]+arr[i])
        maxi = 0
        for i in range(len(arr)):
            ans = (pref[-1]-pref[i])+cont_0[i]
            if ans>maxi:
                maxi = ans
        return maxi
        
