class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        l_sum=sum(cardPoints[:k])
        r_sum=0
        r_index=n-1
        max_sum=l_sum
        for i in range(k-1,-1,-1):
            print(i)
            l_sum-=cardPoints[i]
            r_sum+=cardPoints[r_index]
            r_index-=1
            
            max_sum=max(max_sum, l_sum+r_sum)
        return max_sum

            

        