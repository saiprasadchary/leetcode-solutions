class Solution(object):
    def subarraySum(self, nums, k):
        n=len(nums)
        count=0

        pfs=[0]*n
        pfs[0]=nums[0]
        for i in range(1,n):
            pfs[i]+=pfs[i-1]+nums[i]

        m={}
        for j in range(n):
            if pfs[j]==k:
                count +=1
            key=pfs[j]-k
            if key in m:
                count += m[key]
            if pfs[j] in m:
                m[pfs[j]] += 1
            else:
                m[pfs[j]] = 1

        return count


     


        # count=0
        # for i in range(n):
        #     arrSum=0;
        #     for j in range(i,n):
        #         arrSum+=nums[j] 
        #         if arrSum==k:
        #             count+=1
        # return count

        