class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0;
        j=1;
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1;
            else:
                i+=1
                nums[i]=nums[j];
                j+=1
            
        print(nums)

        return i+1

        # 1, 1, 2
        # i     j




        # st = set()
        # for i in range(len(nums)):
        #     st.add(nums[i])
        # k = len(st)
        # j = 0

        # for x in st:
        #     nums[j] = x
        #     j += 1
        # nums.sort()
        # return k

