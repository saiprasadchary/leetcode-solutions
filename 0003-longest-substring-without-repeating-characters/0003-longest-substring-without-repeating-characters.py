class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        l=r=0
        maxlen=0
        #to check the window duplication we need dictionary
        dict_wind={}
        # it is a two pointer technique to manipulate the wind_size using the dictionary 
        while r<n:
            # the pointer r moves through out the last of the string whereas the l poiner points by skipping the
            # unnecessary values to remove the duplicates in the dictionary
            if s[r] in dict_wind:
                if dict_wind[s[r]]>=l:
                    l=dict_wind[s[r]]+1 # cause as it skips the unnecessary traversal to skip, the pointer l 
                #l should point to the next value to make it sensible(without duplication)

            # the pointer r moves through out the last of the string whereas the l poiner points by skipping the
            # unnecessary values to remove the duplicates in the dictionary
            maxlen=max(r-l+1, maxlen)
            dict_wind[s[r]]=r
            r+=1
        return maxlen

        # dict1={}
        # maxlen=0
        # while r<n:
        #     if s[r] in dict1: 
        #         if dict1[s[r]]>=l:
        #             l=dict1[s[r]]+1
        #     len1=r-l+1;
        #     maxlen=max(len1, maxlen)
        #     dict1[s[r]]=r
        #     r+=1
        # return maxlen


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

        