import heapq

class HeapItem:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, other):
        # Typically, for "top K frequent", we do:
        # "smallest" item is the one with lower freq,
        # or if tie, bigger word lexicographically.
        # Then we keep a min-heap of size k.
        
        if self.count == other.count:
            # For a tie, we want the lexicographically larger word to be "smaller"
            # so that it's popped first. 
            return self.word > other.word
        # If freq is smaller => "worse" => smaller in min-heap sense
        return self.count < other.count

class Solution(object):
    def topKFrequent(self, words, k):
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        # min-heap of size k
        heap = []
        for word, count in freq.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                # if item is "better" than the top => replace
                # "better" means item > heap[0]
                if item > heap[0]:
                    heapq.heapreplace(heap, item)
        res=[]
        while k:
            curr=(heapq.heappop(heap))
            res.append(curr.word)
            k-=1
        return res[::-1]
            




        ##O(nlogK)############
        # heap=[]
        # freq={}
        # n=len(words)
        # res=[]
        # for i in range(n):
        #     freq[words[i]]=freq.get(words[i],0)+1
        
        # for word, freq_w in freq.items():
        #     if(len(heap)<k):
        #     heapq.heappush(heap, (-freq_w, word))
        
               
        # while heap and k>0:
        #     x,y =heapq.heappop(heap)
        #     res.append(y)
        #     k-=1
        # return res
       

        