class Solution(object):
    def frequencySort(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        dict1={};
        for i in s:
            if i not in dict1:
                dict1[i]=1;
            else:
                dict1[i]+=1;

        dict2=(sorted(dict1.items(), key = lambda x: x[1], reverse = True))
        res=\\
        
        for char, freq in dict2:
            res += char * freq  # Correctly repeat char 'freq' times

        return res
        
            
        