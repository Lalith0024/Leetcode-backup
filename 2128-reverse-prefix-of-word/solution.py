class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        l = 0
        while l < len(word) and word[l] != ch:
            l += 1
        if l == len(word):
            return word  # character not found
        ans += word[:l+1][::-1]
        ans += word[l+1:]
        return ans

