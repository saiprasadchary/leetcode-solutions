class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        l1=[];
        n=len(nums2);
        for num in nums1:
            ind = nums2.index(num)
            found = False
           
            for j in range(ind + 1, n):
                if nums2[j] > num:
                    l1.append(nums2[j])
                    found = True
                    break
        
            if not found:
                l1.append(-1)
                
        return l1
        