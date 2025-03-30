import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(arr)
        visited=set()
        heap=[]

        if(len(arr)>1):
            heapq.heappush(heap, ((arr[0]/float(arr[n-1])), 0, n-1))
            visited.add((0,n-1))

            while heap and k>0:
                val, i, j = heapq.heappop(heap)

                if(i+1<n) and (i+1, j) not in visited:
                    frac= (arr[i+1]/float(arr[j]))
                    heapq.heappush(heap, (frac, i+1, j))
                    visited.add((i+1, j))

                if(j-1>=0) and (i, j-1) not in visited:
                    frac=(arr[i])/float(arr[j-1])
                    heapq.heappush(heap, (frac, i, j-1))
                    visited.add((i, j-1))
                k-=1

            return [arr[i],arr[j]]
        else:
            return arr



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