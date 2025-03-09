class Solution(object):
    import heapq
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for i in range(len(nums)):
            
            heapq.heappush(heap, nums[i])
            if(len(heap)>k):
                heapq.heappop(heap)
        return heap[0]

        