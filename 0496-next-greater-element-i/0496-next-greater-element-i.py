class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums1);
        m=len(nums2);
        dictnums1={};
        stack=[]

        for index, val in enumerate(nums1):
            if val not in dictnums1:
                dictnums1[val]=index;
        res=[-1]*n;

        for i in range(m-1,-1,-1):
            curr=nums2[i]
            while stack and stack[-1]<curr:
                stack.pop();
            
            if curr in dictnums1:
                if stack:
                    if stack[-1]>curr:
                        ind=dictnums1[curr];
                        res[ind]=stack[-1];
            stack.append(curr)

        return res



        # dictnums1={};
    
        # for index, val in enumerate(nums1):
        #     if val not in dictnums1:
        #         dictnums1[val]=index;
        # res=[-1]*n;

        # for i in range(m):
        #     if nums2[i] not in nums1:
        #         continue;
        #     for j in range(i+1, m):
        #         if nums2[j]>nums2[i]:
        #             ind=dictnums1[nums2[i]];
        #             res[ind]=nums2[j];
        #             break;
        # return res;
        # for index, val in enumerate(nums1):
        #     if val not in dictnums1:
        #         dictnums1[val]=index;
        # res=[-1]*n;

        # for i in range(m):
        #     if nums2[i] not in nums1:
        #         continue;
        #     for j in range(i+1, m):
        #         if nums2[j]>nums2[i]:
        #             ind=dictnums1[nums2[i]];
        #             res[ind]=nums2[j];
        #             break;
        # return res;
        # for index, val in enumerate(nums1):
        #     if val not in dictnums1:
        #         dictnums1[val]=index;
        # res=[-1]*n;

        # for i in range(m):
        #     if nums2[i] not in nums1:
        #         continue;
        #     for j in range(i+1, m):
        #         if nums2[j]>nums2[i]:
        #             ind=dictnums1[nums2[i]];
        #             res[ind]=nums2[j];
        #             break;
        # return res;
 
        
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
        