class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return '';
        if len(strs)==1:
            return strs[0]
        str2='';
        min_length=float("inf")
        for i in range(len(strs)):
            if len(strs[i])<min_length:
                min_length= len(strs[i]);
        i=0;
        while i < min_length:

            k=strs[0][i];
            for s in strs:
                if s[i]!=k:
                    return str2;
            str2+=k;
            i+=1
        return str2;


