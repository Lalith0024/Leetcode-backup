class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
    # Start by assuming the first string is the common prefix
        prefix = strs[0]
    
    # Loop through all the strings
        for string in strs[1:]:
            # Keep shortening the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
    
        return prefix
        
