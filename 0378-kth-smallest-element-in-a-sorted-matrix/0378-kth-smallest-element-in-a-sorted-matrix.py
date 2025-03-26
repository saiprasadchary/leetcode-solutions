class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #Optimal Approach
        n=len(matrix)
        heap=[]
        # consider the min of k and n ex: if n=3 and k=2, therefore the ele/val should be in the first nested list i.e n=1 or in the second nested list n=2, as they are in the ascending order
        for i in range(min(k,n)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        # accumulating the first values of each list and allso their respective row and col 


        # we collect the columns and push by incrementing 1 and push into the heap to sort.
        for j in range(k):
            val, row, col = heapq.heappop(heap)
            if(col+1< n):
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
        return val
        



###### Brute force's #####
        # n=len(matrix)
        # temp=[]
        # for i in range(n):
        #     temp.extend(matrix[i])
        # temp.sort()
        # return temp[k-1]



        # n=len(matrix)
        # heap=[]
        # for i in range(n):
        #     for j in range(n):
        #         heapq.heappush(heap, -matrix[i][j])
        #         if(len(heap)>k):
        #             heapq.heappop(heap)
        # return -heap[0]




        