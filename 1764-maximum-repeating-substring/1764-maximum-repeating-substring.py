class Solution(object):
    def maxRepeating(self, sequence, word):
        # """
        # :type sequence: str
        # :type word: str
        # :rtype: int
        # """
        # cnt=0
        # n=len(sequence)
        # for i in range(n):
        #     substring=""
        #     for j in range(i,n):
        #         substring+=sequence[j]
        #         if(substring ==word):
        #             cnt+=1
        #         if(len(substring)>len(word)):
        #             break
        # return cnt


        k = 0
        test_str = word
        while test_str in sequence:
            k += 1
            test_str += word
        return k


        # cnt=0
        # n=len(sequence)
        # for i in range(n):
            