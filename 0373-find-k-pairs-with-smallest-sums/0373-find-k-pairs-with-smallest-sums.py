class Solution(object):
    import heapq

    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        # min-heap storing (sum, i, j)
        heap = []
        visited = set()
        result = []

        # push (nums1[0] + nums2[0], 0, 0)
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))

        while heap and len(result) < k:
            curSum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # Next candidate (i+1, j)
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))

            # Next candidate (i, j+1)
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))

        return result
        

        