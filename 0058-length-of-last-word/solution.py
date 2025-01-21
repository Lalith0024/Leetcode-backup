class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        a = s.split()
        return (len(a[-1]))

        
