class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0;
        
        mini=prices[0];
        for i in range(1, len(prices)):
            if prices[i]-mini>0:
                profit=max(profit, prices[i]-mini)
            else:
                mini=min(mini, prices[i]);
        return profit;


#         # profit=0;
#         # for i in range(len(prices)):
#         #     for j in range(i+1, len(prices)):
#         #         if prices[i]< prices[j]:
#         #             temp=prices[j]-prices[i];
#         #             profit=max(temp, profit);

#         # return profit;


#         profit=0;
#         smallValInd=-1;

#         mini=float("inf")
#         for i in range(len(prices)-1):
#             if prices[i]<mini:
#                 mini=prices[i];
#                 smallValInd=i;
#                 print(mini, smallValInd)
#         print(mini, smallValInd)

#         for i in range(smallValInd, len(prices)):
#             if prices[i]-mini > 0:
#                 temp=prices[i]-mini;
#                 profit=max(profit, temp);
#         return profit;




        
        
        