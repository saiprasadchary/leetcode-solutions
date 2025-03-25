class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        freq={}
        heap=[]
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if(len(heap)>k):
                heapq.heappop(heap)
        j=0
        print(heap)
        while heap:
            _, val = heappop(heap)
            nums[j]=val
            j+=1

        return nums[:j]










        # heap=[]
        # n=len(nums)
        # freq={}
        # for i in range(n):
        #    freq[nums[i]]=freq.get(nums[i],0)+1
        
        # for x,v in freq.items():
        #     heapq.heappush(heap, (v,x))
        #     if(len(heap)>k):
        #         heapq.heappop(heap)
        # nums=[]
        # while heap:
        #     nums.append(heapq.heappop(heap)[1])
        # return nums

















        