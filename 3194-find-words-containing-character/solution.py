class Solution:
    def findWordsContaining(self, w: List[str], x: str) -> List[int]:
        return [i for i,v in enumerate(w) if x in v]
