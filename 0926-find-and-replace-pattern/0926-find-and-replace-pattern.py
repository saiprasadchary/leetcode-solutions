class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        l1=[];
        def func(pattern, word): 
            pattern_i={};
            i_pattern={};
            for u, v in zip(pattern, word):
                if u in pattern_i and pattern_i[u]!=v:
                    return False
                elif v in i_pattern and i_pattern[v]!=u:
                    return False;
                i_pattern[v]=u;
                pattern_i[u]=v;
            return True;
        for word in words:
            if func(pattern, word):
                l1.append(word);
        return l1;



        