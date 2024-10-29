class Solution(object):
    def rotate(self, nums, k):
        """
        
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n

        if k==0:
            return nums;
        temp=[]
        for i in range(n-k):
            temp.append(nums[i]);
        print(temp)
        
        for j in range(n-k, n):
            nums[j-(n-k)]=nums[j];
        y=0
        for x in range(k, n):
            nums[x]=temp[y]
            y+=1
        
        # l1=nums[n-k:]+nums[:n-k];
        # for i in range(len(l1)):
        #     nums[i]=l1[i];
        
        
        # for i in range(n-k):
        #     temp=nums[0]
        #     for j in range(1, len(nums)):
        #         nums[j-1]=nums[j];
            
        #     nums[len(nums)-1]=temp
        #     print(nums)
        
        
        
        