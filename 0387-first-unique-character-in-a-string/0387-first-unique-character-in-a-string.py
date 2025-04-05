class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}

        for char in s:
            # count the freq of each character
            freq[char]=freq.get(char, 0)+1
            #freq={"s":1 }

        
        for i in range(len(s)):
            if(freq[s[i]]==1):
                return i
                
        return -1
        