class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        \\\
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        \\\
        # n=len(nums1);
        # m=len(nums2)
        # while m-1:
        #     if nums1[n-1] in nums2:
        #         if stack:
        #             if stack[-1]>nums
        #         else:
        #             res[n-1]=-1;





        
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
        