class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1=0
        cand2=0
        cnt1=0
        cnt2=0
        n=len(nums)
        for i in range(n):
            if(cnt1==0) and nums[i]!=cand2:
                cand1=nums[i]
                cnt1+=1
            elif(cnt2==0) and nums[i]!=cand1:
                cand2=nums[i]
                cnt2+=1
            elif(nums[i]==cand1):
                cnt1+=1
            elif(nums[i]==cand2):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1=0
        cnt2=0
        for j in range(n):
            if nums[j]==cand1:
                cnt1+=1
            elif nums[j]==cand2:
                cnt2+=1

        res=[]

        if(cnt1>n/3):
            res.append(cand1)
        if(cnt2>n/3):
            res.append(cand2)
        return res
    

        