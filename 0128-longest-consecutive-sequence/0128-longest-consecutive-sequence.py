class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        longest=1;
        c=1
        s_nums=sorted(nums);
        print(s_nums)
        for i in range(1, len(nums)):
            start=s_nums[i]
            if s_nums[i]==s_nums[i-1]:
                continue;
            elif s_nums[i-1]+1==s_nums[i]:
                c+=1;
                print(c)
                longest=max(longest,c);
            else:
                c=1
            
        return longest
            

        # s=set(nums);
        # longest=0;
        # for i in range(len(nums)):
        #     if nums[i]-1 not in s:
        #         c=1;
        #         k=nums[i]+1

        #         while k in s:
        #             c+=1;
        #             k+=1
        #         longest=max(longest,c);
        # return longest;

        