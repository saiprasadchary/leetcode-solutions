class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap=[]
        n=len(nums)
        freq={}
        for i in range(n):
           freq[nums[i]]=freq.get(nums[i],0)+1
        
        for x,v in freq.items():
            heapq.heappush(heap, (v,x))
            if(len(heap)>k):
                heapq.heappop(heap)
        print(heap)
        l1=[]
        while heap:
            l1.append(heapq.heappop(heap)[1])
        return l1
        