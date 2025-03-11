class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        #heap implementation
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        heap=[]
        for char, frequ in freq.items():
            heapq.heappush(heap, (-frequ, char))
        res=""
        while heap:
            freq_val, character = heapq.heappop(heap)
            print(-freq_val, character)
            z=-freq_val
            for j in range(z):
                res+=(character)
        return res


        # dict1={};
        # for i in s:
        #     if i not in dict1:
        #         dict1[i]=1;
        #     else:
        #         dict1[i]+=1;

        # dict2=(sorted(dict1.items(), key = lambda x: x[1], reverse = True))
        # res=""
        # print((dict2))
        
        # for char, freq in dict2:
        #     res += char * freq  # Correctly repeat char 'freq' times

        # return res
        
            
        