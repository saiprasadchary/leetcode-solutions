class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        l1=s.split(" ")
        if len(pattern)!=len(l1):
            return False;
        else:
            wordToChar={};
            charToWord={};

            for x,y in zip(pattern, l1):
                if x in charToWord and charToWord[x] != y:
                    return False;
                if y in wordToChar and wordToChar[y]!= x:
                    return False;
                charToWord[x] = y;
                wordToChar[y] =x;
            return True 




        