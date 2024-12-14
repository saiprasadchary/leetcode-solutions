class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums1);
        m=len(nums2);
        dictnums1={};
    
        for index, val in enumerate(nums1):
            if val not in dictnums1:
                dictnums1[val]=index;
        res=[-1]*n;

        for i in range(m):
            if nums2[i] not in nums1:
                continue;
            for j in range(i+1, m):
                if nums2[j]>nums2[i]:
                    ind=dictnums1[nums2[i]];
                    res[ind]=nums2[j];
                    break;
        return res;
                


        # stack=[];
        # ans=[]
        # for i in range(len(nums2)-1,-1,-1):
        #     temp=nums2[i]
        #     if  temp in nums1:
        #         if stack:
        #             while stack:
        #                 if stack[-1]>temp:
        #                     ans.append(stack[-1]);
        #                     break
        #                 else:
        #                     stack.pop()
        #         else:
        #             ans.append(-1)
        #             stack.append(nums2[i]);
        #     else:
        #         stack.append(nums2[i])
        # return ans;
        
        # l1=[];
        # n=len(nums2);
        # for num in nums1:
        #     ind = nums2.index(num)
        #     found = False
           
        #     for j in range(ind + 1, n):
        #         if nums2[j] > num:
        #             l1.append(nums2[j])
        #             found = True
        #             break
        #     if not found:
        #         l1.append(-1)
                
        # return l1
        