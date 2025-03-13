class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap=[]
        freq={}
        n=len(words)
        res=[]
        for i in range(n):
            freq[words[i]]=freq.get(words[i],0)+1
        
        for word, freq_w in freq.items():
            heapq.heappush(heap, (-freq_w, word))
               
        while k>0:
            x,y=heapq.heappop(heap)
            res.append(y)
            k-=1
        return res
       

        