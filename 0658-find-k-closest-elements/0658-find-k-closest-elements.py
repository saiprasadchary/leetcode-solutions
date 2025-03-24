class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap=[]
        n=len(arr)

        for i in range(n):
            heapq.heappush(heap, (-abs(arr[i]-x), -arr[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        j=0
    
        resHeap=[]
        while heap:
            _, negval=heapq.heappop(heap)
            heapq.heappush(resHeap, -negval)
        
        while resHeap:
            arr[j]=heapq.heappop(resHeap)
            j+=1
        
        return arr[:k]












        # n=len(arr)
        # res=[]
        # heap=[]
        # for i in range(n):
        #     dist=abs(arr[i]-x)
        #     heapq.heappush(heap, (-dist, -arr[i]))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # print(heap)

        # while heap:
        #     x,y=heapq.heappop(heap)
        #     res.append(-y)
        
        # f_res=[]
        # min_heap=[]
        # for x in res:
        #     heapq.heappush(min_heap, x)
        # while min_heap:
        #     f_res.append(heapq.heappop(min_heap))
        # return f_res
            

        