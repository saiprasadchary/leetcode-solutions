class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        n=len(nums)
        for i in range(n):
           freq[nums[i]]=freq.get(nums[i],0)+1
        heap=[]
        for val,frequ in freq.items():
            heapq.heappush(heap, (frequ,-val))
            # if the values are tied, consider the frequ (inorder to satisfy the max frequ first we add the negative)
        res=[]
        while heap:
            frequency, value=heapq.heappop(heap)
            for j in range(frequency):
                res.append(-value)
        return res
        