class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n=len(arr)
        res=[]
        heap=[]
        for i in range(n):
            dist=abs(arr[i]-x)
            heapq.heappush(heap, (-dist, -arr[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)

        while heap:
            x,y=heapq.heappop(heap)
            res.append(-y)
        return sorted(res)
            

        