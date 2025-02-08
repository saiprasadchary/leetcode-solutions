class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        l=0
        r=0
        dict1={}
        maxlen=0
        while r<n:
            
            if s[r] in dict1:
                if dict1[s[r]]>=l:
                    l=dict1[s[r]]+1
            len1=r-l+1;
            maxlen=max(len1, maxlen)
            dict1[s[r]]=r
            r+=1
        return maxlen











        # n=len(s)
        # maxlen=0;
        # for i in range(n):
        #     l1=[];
        #     for j in range(i, n):
        #         if s[j] in l1:
        #             break;
        #         len1=j-i+1;
        #         maxlen=max(maxlen,len1)
        #         l1.append(s[j])
        # return maxlen;

        