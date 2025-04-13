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
            if(nums[i]==cand1):
                cnt1+=1
            elif(nums[i]==cand2):
                cnt2+=1
            
            elif(cnt1==0):
                cand1=nums[i]
                cnt1+=1
            elif(cnt2==0 and cand1!=nums[i]):
                cand2=nums[i]
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
            
        c1=0
        c2=0
        print(cand1)
        print(cand2)
        for i in range(n):
            if nums[i]==cand1:
                c1+=1
            if(nums[i]==cand2):
                c2+=1

        l1=[]   
        if c1>(len(nums)/3):
            l1.append(cand1)
        if c2>(len(nums)/3) and cand1!=cand2:
            l1.append(cand2)
        return l1
    

        