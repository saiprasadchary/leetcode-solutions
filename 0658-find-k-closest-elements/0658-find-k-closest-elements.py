import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Step 1: Identify the k closest elements using a max-heap
        max_heap = []
        for val in arr:
            dist = abs(val - x)
            # push ( -distance, -value ) to simulate a max-heap by distance
            heapq.heappush(max_heap, (-dist, -val))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Step 2: Extract those k elements (unsorted)
        closest_k = []
        while max_heap:
            distVal, negVal = heapq.heappop(max_heap)
            closest_k.append(-negVal)  # revert to original value
        
        # Step 3: Use a min-heap to sort those k elements in ascending order
        #         without calling sorted()
        min_heap = []
        for num in closest_k:
            heapq.heappush(min_heap, num)
        
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))
        
        return result