class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        finalArr=nums1+nums2
        finalArr.sort()
        avg=0.0
        n=len(finalArr)
        
        if(n%2==0):
            i=n//2
            sum1=finalArr[i]+finalArr[i-1]

            print(finalArr[i], finalArr[i-1])
            print(sum1)
            avg=float(sum1/2.0)
            return avg
        else:
            return finalArr[n/2]
        