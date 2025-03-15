class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten=0,0
        #twenty is not needed because that is the far end bill

        for i in range(len(bills)):
            if(bills[i]==5):
                five+=1
            elif(bills[i]==10):
                if(five):
                    five-=1
                    ten+=1
                else:
                    return False
            elif(bills[i]==20):
                if(five and ten):
                    ten-=1
                    five-=1
                elif(five>=3):
                    five-=3
                else:
                    return False
        return True
        