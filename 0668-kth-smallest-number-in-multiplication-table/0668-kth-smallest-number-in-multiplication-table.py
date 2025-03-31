class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo, hi = 1, m * n  # The possible range of values in the table.
        
        # Helper function: counts numbers in the multiplication table <= x.
        def countLE(x):
            count = 0
            # For each row i (1-indexed), the number of elements in row i that are <= x is min(n, x//i)
            for i in range(1, m+1):
                count += min(n, x // i)
            return count
        
        # Binary search for the smallest value such that there are at least k numbers <= that value.
        while lo < hi:
            mid = (lo + hi) // 2
            if countLE(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo



    # Brute 
        # mat=[]
        
        # for i in range(1, m+1):
        #     temp=[]
        #     for j in range(1, n+1):
        #         temp.append((i)*(j))
        #     mat.append(temp)
        
        # heap=[]
        # for firstInd in range(m):
        #     heapq.heappush(heap, (mat[firstInd][0], firstInd, 0))
        
        # while heap and k>0:
        #     val, row, col=heapq.heappop(heap)
        #     if(col+1<n):
        #         heapq.heappush(heap, (mat[row][col+1], row, col+1))
        #     k-=1
        # return val





    #brute force approach
        # mat=[]
        
        # for i in range(1, m+1):
        #     temp=[]
        #     for j in range(1, n+1):
        #         temp.append((i)*(j))
        #     mat.append(temp)

        # l1=[]
        # for x in mat:
        #     l1.extend(x)
        # l1.sort()
        # return l1[k-1]
        