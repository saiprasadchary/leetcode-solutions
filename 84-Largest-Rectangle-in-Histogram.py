class Solution(object):
    def largestRectangleArea(self, heights):
        \\\
        :type heights: List[int]
        :rtype: int
        \\\
        # Stack to keep track of indices of the histogram's bars
        stack = []
        max_area = 0
        index = 0
        
        # Loop through all bars of the histogram
        while index < len(heights):
            # If stack is empty or current bar is higher than the bar at stack top
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Calculate area with the bar at the top of the stack as the smallest bar
                top_of_stack = stack.pop()
                # Area = height of the popped bar * width
                area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
                # Update max_area if current area is larger
                max_area = max(max_area, area)
        
        # Now, pop the remaining bars from stack and calculate area
        while stack:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
        
        return max_area


