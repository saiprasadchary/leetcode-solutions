class Solution:
    def merge(self, intervals):

        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        res=[]
        i=0
        n=len(intervals)
        temp=intervals[0]

        #we just need to check if there is a overlapping or not
        #consider the initial values as temp used for comparisions
         #_________Overlap comparision is checked as if the temp is to the roght of the current arr values and arr[i][0]<=temp[i]__

        while i< n:

            if(intervals[i][0]<=temp[1]):
                #temp[0]=min(intervals[i][0], temp[0])
                temp[1]=max(intervals[i][1], temp[1])

            else:
                res.append(temp)
                temp=intervals[i]
            i+=1
        res.append(temp)

        return res



        
        