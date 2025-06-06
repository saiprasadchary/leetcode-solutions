class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        if n==1:
            return 0
        cnt=1

        
        intervals.sort(key=lambda x:x[1])
        lastInd=intervals[0][1]

        for i in range(1, n):
            if(intervals[i][0]>=lastInd):
                cnt+=1
                lastInd=intervals[i][1]

        return n-cnt