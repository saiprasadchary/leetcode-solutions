class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        #we need to run the pointer to the point where the merging happens
        
        i=0
        res=[]
        n=len(intervals)

        # left part to append the safe intervals in the res array - traversing
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
            
        # Now overlaping part here the overlapping is alreadily defined by above condition check
            # all we need to do is to find where the second value in the new interval and the first value in the current array are <=
             #consider interval [3, 3] and newInterval [3, 3] 
        while i< n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0], intervals[i][0])
            newInterval[1]=max(newInterval[1], intervals[i][1])
            i+=1
        res.append(newInterval)

        # right most partis the remaining part so no need extra constraint
        while i<n:
            res.append(intervals[i])
            i+=1

        return res
        
