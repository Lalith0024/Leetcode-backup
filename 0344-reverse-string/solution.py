class Solution:
    def reverseString(self, s: List[str]) -> None:
        high = len(s)-1
        low = 0
        while low<=high:
            s[low],s[high] = s[high],s[low]
            low+=1
            high-=1


