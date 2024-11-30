class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Finding the shortest string in the list
        min_length = min(len(s) for s in strs)
        
        lcp = ""
        for i in range(min_length):
            # Take the current character from the first string
            current_char = strs[0][i]
            
            # Compare this character with the character at the same position in all other strings
            for s in strs:
                if s[i] != current_char:
                    return lcp
            
            # If current_char is present at position i in all strings, add it to the result
            lcp += current_char
        
        return lcp