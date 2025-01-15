class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        return self.recPT([[1]], numRows-1)

    def recPT(self, pT, remRows):
        if remRows == 0:
            return pT
        newR = [1]
        for i in range(1, len(pT[-1])):
            newR.append(pT[-1][i-1] + pT[-1][i])    #ith number in new row
        newR.append(1)
        pT.append(newR)
        return self.recPT(pT, remRows - 1)
        