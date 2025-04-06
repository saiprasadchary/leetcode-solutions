class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n=len(hand)
        if n%groupSize!=0:
            return False
        freq={}
        for i in range(n):
            freq[hand[i]]=freq.get(hand[i], 0)+1
        
        freqKeys=sorted(freq.keys())

        for val in freqKeys:

            while freq[val]:

                for k in range(1, groupSize):
                    if(val+k not in freq) or freq[val+k]==0:
                        return False
                    freq[val+k]-=1

                freq[val]-=1

        return True

        