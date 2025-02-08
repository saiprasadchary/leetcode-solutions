class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        maxlen=0;
        for i in range(n):
            l1=[];
            for j in range(i, n):
                if s[j] in l1:
                    break;
                len1=j-i+1;
                maxlen=max(maxlen,len1)
                l1.append(s[j])
        return maxlen;

        