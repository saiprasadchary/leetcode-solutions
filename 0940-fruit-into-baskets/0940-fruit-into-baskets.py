class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n=len(fruits)
        maxlen=0
        r=l=0
        freq={}
        
        while r<n:
            freq[fruits[r]]=freq.get(fruits[r],0)+1

            if(len(freq)>2):
                freq[fruits[l]]-=1
                if(freq[fruits[l]]==0):
                    del freq[fruits[l]]
                l+=1

            maxlen=max(maxlen, r-l+1)
            r+=1
        return maxlen



        