class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # freq={}
        # max_freq=0
        # l=0
        # r=0
        # longest=0
        # n=len(s)
        # while r<n:
        #     freq[s[r]]=freq.get(s[r],0)+1
        #    # max_freq=max(max_freq, freq[s[r]])
        #     max_freq=max(freq.values())

        #     wind=r-l+1
        #     if wind-max_freq<=k:
        #         longest=max(longest,wind)
        #     else:
        #         freq[s[l]]-=1
        #         l+=1;
        #     r+=1
        # return longest


        #better approach
        l=r=0
        max_len=0
        freq={}
        n=len(s)

        while r<n:
            freq[s[r]]=freq.get(s[r],0)+1
            max_freq=max(freq.values())
            repl_pos=(r-l+1)-max_freq

            while(repl_pos>k):
                freq[s[l]]-=1
       
                if freq:
                    max_freq=max(freq.values())
                else: 
                    max_freq=0
                l+=1
                repl_pos=(r-l+1)-max_freq

            if(repl_pos<=k):
                max_len=max(r-l+1, max_len)
            r+=1
        return max_len
                




        # brute force approach, everytime we get the updated freqvalues in every iteration to compare with the k through condition len-max_freq 
        # n = len(s)
        # max_len = 0
        # for i in range(n):
        #     freq={}
        #     for j in range(i,n):
        #         #freq[ord(s[j])-26]=freq.get(ord(s[j])-26 ,0)+1
        #         freq[s[j]]=freq.get(s[j] ,0)+1  
        #         max_freq=max(freq.values())
        #         replacements=(j-i+1)-max_freq
        #         if replacements<=k:
        #             max_len=max(j-i+1, max_len)
        #         else:
        #             break
        # return max_len
       


                