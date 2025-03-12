class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            word += ''.join(chr((ord(c) - 97 + 1) % 26 + 97) for c in word)
        return word[k - 1]
            
