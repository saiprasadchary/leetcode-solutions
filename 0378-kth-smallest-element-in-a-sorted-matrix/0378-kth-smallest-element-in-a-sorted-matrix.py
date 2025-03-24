class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        heap=[]
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, -matrix[i][j])
                if(len(heap)>k):
                    heapq.heappop(heap)
        return -heap[0]




        