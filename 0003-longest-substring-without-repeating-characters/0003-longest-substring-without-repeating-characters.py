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
                if dict_wind[s[r]]>=l: #this check is to make sure the traversal i.e by moving the l pointer to he forward not backwards
                    l=dict_wind[s[r]]+1 # cause as it skips the unnecessary traversal to skip, the pointer l 
                #l should point to the next value to make it sensible(without duplication)

            # the pointer r moves through out the last of the string whereas the l poiner points by skipping the
            # unnecessary values to remove the duplicates in the dictionary
            
            dict_wind[s[r]]=r
            maxlen=max(r-l+1, maxlen)

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



        ###### this solving resembles as a similar way as for the maxSum of distinct subarrays #####

        # nums=s
        # n=len(nums)
        # l=r=0
        # maxWind=0
        # freq={}
        # while r<n:
        #     freq[nums[r]]=freq.get(nums[r],0)+1
        #     while(freq[nums[r]]>1):
        #         freq[nums[l]]-=1
        #         l+=1
        #     #if(len(freq)==r-l+1):
        #     maxWind=max(maxWind, r-l+1)
        #     r+=1
        # return maxWind


        maxLen=0
        l=r=0
        arr=s
        n=len(arr)
        freq={}
        while r<n:
            if(arr[r] in freq):
                if(freq[arr[r]]>=l):
                    l=freq[arr[r]]+1
                
            freq[arr[r]]=r
            print(maxLen, r-l+1)
            maxLen=max(maxLen, r-l+1)
            
            r+=1
        return maxLen
