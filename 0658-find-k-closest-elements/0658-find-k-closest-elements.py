import bisect, heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        # 1) Find insertion point or closest position of x in arr
        pos = bisect.bisect_left(arr, x)
        # pick a window from max(0, pos-k) to min(n-1, pos+k)
        left = max(0, pos - k)
        right = min(n-1, pos + k)
        
        # 2) Use a max-heap of size k on just these ~2k elements
        #    store (-diff, -val) so we pop the biggest diff first
        heap = []
        for i in range(left, right + 1):
            diff = abs(arr[i] - x)
            heapq.heappush(heap, (-diff, -arr[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3) Pop from the heap into a list, then sort
        result = []
        while heap:
            diff, negval = heapq.heappop(heap)
            result.append(-negval)
        
        result.sort()
        return result