import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        heap = []
        
        for i in range(n):
            for j in range(i+1, n):
                frac = (arr[i]) / float(arr[j])

                heapq.heappush(heap, (-frac, arr[i], arr[j]))
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return [heap[0][1], heap[0][2]]