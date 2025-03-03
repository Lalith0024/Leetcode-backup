class Solution(object):
    def checkIfPangram(self, sentence):
        new = set(sentence)
        if len(new)==26:
            return True
        else:
            return False
        
