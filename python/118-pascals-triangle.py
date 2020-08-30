v = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]]

for i in v:
    print(i)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev_row = None
        result = []
        for n in range(1,numRows+1):
            row = [1 for t in range(n)]
            for i in range(1, n-1):
                row[i] = prev_row[i-1] + prev_row[i]
            prev_row = row
            result.append(row)
        return result
