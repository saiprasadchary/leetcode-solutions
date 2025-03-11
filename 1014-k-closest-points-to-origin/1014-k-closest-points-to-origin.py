class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i in range(len(points)):
            x1=points[i][0]
            y1=points[i][1]
            sum1=x1**2 + y1**2
            distance=math.sqrt(sum1)
            heapq.heappush(heap, (-distance, points[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        while heap:
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res


        