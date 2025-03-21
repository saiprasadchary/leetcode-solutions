class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq={}
        max_freq=0
        l=0
        r=0
        longest=0
        n=len(s)
        while r<n:
            freq[s[r]]=freq.get(s[r],0)+1
            max_freq=max(max_freq, freq[s[r]])
            #max_freq=max(freq.values())

            wind=r-l+1
            if wind-max_freq<=k:
                longest=max(longest,wind)
            else:
                freq[s[l]]-=1
                l+=1;
            r+=1
        return longest


        #------better and with "If" it becomes optimal approach-----
        # l=r=0
        # max_len=0
        # freq={}
        # n=len(s)

        # while r<n:
        #     freq[s[r]]=freq.get(s[r],0)+1
        #     max_freq=max(freq.values())

        #     #while((r-l+1)-max_freq>k):
        #     if((r-l+1)-max_freq>k):
        #         freq[s[l]]-=1
        #         if(freq[s[l]]==0): del freq[s[l]]
        #         # here the fresh max_freq should be calculated irrespective of the exising as the manipulation is done in freq or the dictionary to have the updated maxfreq of that segment
        #         max_freq=max(freq.values())
        #         l+=1

        #     if((r-l+1)-max_freq<=k):
        #         max_len=max(r-l+1, max_len)
        #     r+=1
        # return max_len
                



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

    #     n=len(s)
    #     maxlen=0
    #     for i in range(n):
    #         freq={}
    #         for j in range(i,n):
    #             freq[s[j]]=freq.get(s[j],0)+1
                
    #             acc_repl=(j-i+1)-max(freq.values())
    #             if(acc_repl<=k):
    #                 maxlen=max(maxlen, j-i+1)
    #             else:
    #                 break
    #     return maxlen



        # l=r=0
        # freq={}
        # n=len(s)
        # maxlen=0

        # while r<n:

        #     freq[s[r]]=freq.get(s[r],0)+1
        #     acc_repl=(r-l+1)-max(freq.values())

        #     if (r-l+1)-max(freq.values())>k:
        #         freq[s[l]]-=1
        #         if(freq[s[l]]==0):
        #             del freq[s[l]]
        #         l+=1

        #     if((r-l+1)-max(freq.values())<=k):
        #         maxlen=max(maxlen, r-l+1)
        #     r+=1

        # return maxlen
            
       


                