class Solution(object):
    
    def nextGreatestLetter(self, letters, target):
        ans = letters[0]
        for i in range(len(letters)):
            if letters[i]>target:
                ans = letters[i]
                break
        return ans
        
