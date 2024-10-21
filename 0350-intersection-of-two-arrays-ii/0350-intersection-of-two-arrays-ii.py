class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1=[];
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                l1.append(nums1[i]);
                nums2.remove(nums1[i])
                
        return (l1)





        # l1=[];
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j]:
        #             l1.append(nums1[i]);
        #             nums2[j]=None;
        #             break
        # return l1