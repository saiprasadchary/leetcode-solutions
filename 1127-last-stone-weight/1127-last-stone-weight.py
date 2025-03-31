class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap=[]
        n=len(stones)

        for i in range(n):
            heapq.heappush(heap, -stones[i])
        print(heap)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            rem=x-y

            if rem:
                heapq.heappush(heap, -rem)

        if len(heap)==0:
            return 0
        else:
            return -heap[0]  