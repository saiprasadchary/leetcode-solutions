class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)

        # initial consideration of sum could be initiated to the l_sum  [_______]____________ , _____]_____[_ .. so on therefore forloop starts in reverse from k
        l_sum=sum(cardPoints[:k])
        r_sum=0
        # this palys a pointer role to consider from end to the right_sum to K
        r_index=n-1
        max_sum=l_sum

        for i in range(k-1,-1,-1):

            # removal from left_Sum
            l_sum-=cardPoints[i]

            # adding into the right_sum
            r_sum+=cardPoints[r_index]
            
            r_index-=1
            
            max_sum=max(max_sum, l_sum+r_sum)

        return max_sum

            

        