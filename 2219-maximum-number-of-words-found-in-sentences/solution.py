class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lengths = [len(i.split(' ')) for i in sentences]
        return max(lengths)
        #do it by another method
        
        
