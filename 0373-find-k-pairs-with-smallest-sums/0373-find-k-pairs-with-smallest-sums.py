class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n=len(nums1)
        m=len(nums2)
        heap=[]
        visited=set()
        i=j=0
        heapq.heappush(heap, ((nums1[i]+nums2[j]), i,j))
        visited.add((i,j))
        #k-=1
        res=[]
        while k>0 and heap:
            _,i,j=heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if(i+1<n and (i+1, j) not in visited):
                heapq.heappush(heap, ((nums1[i+1]+nums2[j]), i+1, j))
                visited.add((i+1,j))
            
            if(j+1<m and (i,j+1) not in visited):
                heapq.heappush(heap, ((nums1[i]+nums2[j+1]), i, j+1))
                visited.add((i,j+1))
            k-=1
        return res
        # heap=[]
        # res=[]
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         res.append([nums1[i], nums2[j]])
        #         sum1=nums1[i]+nums2[j]
        #         heapq.heappush(heap, (-sum1, [nums1[i], nums2[j]]))
        #         if(len(heap)>k):
        #             heapq.heappop(heap)

        # heap2=[]
        # res=[]
        # while heap:
        #     x, list1 = heapq.heappop(heap)
        #     sum1=-x
        #     heapq.heappush(heap2, (sum1, list1))
        # while heap2:
        #     res.append(heap2[0][1])
        #     heapq.heappop(heap2)
        # return res
        

        