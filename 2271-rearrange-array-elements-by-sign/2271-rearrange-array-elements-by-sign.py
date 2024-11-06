class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # i=0;
        # j=1
        # while i<len(nums)-1 and j < len(nums):
        #     if nums[i]<0 and nums[j]>0:
        #         nums[i], nums[j]=nums[j], nums[i]
        #         i+=2;
        #         j+=2
        #     elif nums[i] >0 and nums[j]>0:
        #         j+=1;
        #     elif nums[i]>0  and nums[j]<0 and i+1<j:
        #         nums[i+1], nums[j]= nums[j], nums[i+1];
        #         i+=2;
        #         j+=1;
        #     elif nums[i]>0 and nums[j]<0 and i+1==j:
        #         i+=2;
        #         j+=2
            
        # return nums


        neg_arr = []
        pos_arr = []
        

        # Separate negative and positive numbers
        for num in nums:
            if num < 0:
                neg_arr.append(num)
            else:
                pos_arr.append(num)

        k=0;
        while k < len(pos_arr):
            nums[2*k]= pos_arr[k];
            nums[2*k +1] = neg_arr[k];
            k+=1
        return nums






























