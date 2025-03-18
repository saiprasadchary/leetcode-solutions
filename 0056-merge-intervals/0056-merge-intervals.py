class Solution:
    def merge(self, intervals):
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        res = []
        n = len(intervals)
        
        # If no intervals, return empty
        if n == 0:
            return res
        
        # Initialize 'temp' to the first interval
        temp = [intervals[0][0], intervals[0][1]]
        i = 1  # we'll process from the second interval onward
        
        # Single while loop to merge
        while i < n:
            # If intervals[i] overlaps with 'temp'
            if intervals[i][0] <= temp[1]:
                # Merge by updating the end
                temp[1] = max(temp[1], intervals[i][1])
            else:
                # No overlap, push the current 'temp' to 'res' and reset
                res.append(temp)
                temp = [intervals[i][0], intervals[i][1]]
            i += 1
        
        # After loop, append the last 'temp'
        res.append(temp)
        return res