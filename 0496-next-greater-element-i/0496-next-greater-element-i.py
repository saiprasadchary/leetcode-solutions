class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # since n1 is a subset of n2:
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ind=nums2.index(nums1[i]);
                print(ind);
                
                    
                while ind<len(nums2):
                    if ind==len(nums2)-1:
                        nums1[i]=-1
                        break
                    if ind<= len(nums2) and nums2[ind+1] > nums1[i]:
                        nums1[i]=nums2[ind+1];
                        break;
                        
                    else:
                        ind+=1
                else:
                    nums1[i]=-1
                    
        return nums1
        