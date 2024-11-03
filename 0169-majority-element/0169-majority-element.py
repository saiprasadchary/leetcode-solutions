class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate=0;
        count=0;

        for curr_num in nums:
            if count==0:
                candidate=curr_num;
            if curr_num==candidate:
                count+=1;
            else:
                count-=1
        return candidate;




        # dict={};
        # for i in  nums:
        #     if i not in dict:
        #         dict[i]=1;
        #     else:
        #         dict[i]+=1;
        # ans=-1
        # max_val = float('-inf')
        # for k , v in dict.items():
        #     if v>max_val:
        #         max_val=v;
        #         ans=k;
        # return ans

        
        # if nums is None:
        #     return None;
        # s=set(nums);
        # c=0
        # c1=0;
        # candidate=nums[0]
        # for i in nums:
        #     if i in s:
        #         c = nums.count(i) 
        #         if c > c1:
        #             c1 = c
        #             candidate = i
        #         s.remove(i)
        # return candidate;

