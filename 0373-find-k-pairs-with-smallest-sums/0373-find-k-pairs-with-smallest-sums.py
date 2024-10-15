import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Edge case handling
        if not nums1 or not nums2 or k == 0:
            return []
        
        # Min-heap to store the smallest pairs
        heap = []
        
        # Initial population of the heap with the smallest pairs (nums1[i], nums2[0])
        # i.e., pair each element in nums1 with the first element in nums2
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)
        
        result = []
        
        # Extract the k smallest pairs
        while heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # If possible, push the next pair (nums1[i], nums2[j+1]) into the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result

            

        