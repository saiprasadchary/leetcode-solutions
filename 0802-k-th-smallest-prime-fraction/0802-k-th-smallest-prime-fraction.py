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
        visited = set()
        
        # Start with the pair (0, n-1)
        heapq.heappush(heap, (arr[0] / float(arr[n-1]), 0, n-1))
        visited.add((0, n-1))
        
        # Pop k-1 times; the kth pop will give us the kth smallest fraction.
        for _ in range(k - 1):
            frac, curr_i, curr_j = heapq.heappop(heap)
            
            # Neighbor: move down (increase row index)
            if curr_i + 1 < n and (curr_i + 1, curr_j) not in visited:
                heapq.heappush(heap, (arr[curr_i+1] / float(arr[curr_j]), curr_i+1, curr_j))
                visited.add((curr_i+1, curr_j))
            
            # Neighbor: move left (decrease column index)
            if curr_j - 1 >= 0 and (curr_i, curr_j - 1) not in visited:
                heapq.heappush(heap, (arr[curr_i] / float(arr[curr_j-1]), curr_i, curr_j-1))
                visited.add((curr_i, curr_j-1))
        
        # The kth smallest fraction is at the top of the heap now.
        frac, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]



    # Brute force approach
        # n = len(arr)
        # heap = []
        
        # for i in range(n):
        #     for j in range(i+1, n):
        #         frac = (arr[i]) / float(arr[j])

        #         heapq.heappush(heap, (-frac, arr[i], arr[j]))
        #         if len(heap) > k:
        #             heapq.heappop(heap)
        
        # return [heap[0][1], heap[0][2]]