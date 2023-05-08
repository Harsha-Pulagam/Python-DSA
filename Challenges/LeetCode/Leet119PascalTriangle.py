class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        ans = [1]*(n+1)
        for i in range(2, n+1) :
            for j in range(1, i) :
                ans[i-j]+= ans[i-j-1]
                print(ans)
        return ans
