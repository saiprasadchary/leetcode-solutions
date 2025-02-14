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
            wind=r-l+1
            if wind-max_freq<=k:
                longest=max(longest,wind)
            else:
                freq[s[l]]-=1
                l+=1;
            r+=1
        return longest


                