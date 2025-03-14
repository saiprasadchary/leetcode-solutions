class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        sum1=0
        j=len(numbers)-1
        while i<j:
            sum1=numbers[i]+numbers[j]
            if(sum1==target):
                return [i+1,j+1]
            if(sum1<target):
                i+=1
            if(sum1>target):
                j-=1
            
        return []
