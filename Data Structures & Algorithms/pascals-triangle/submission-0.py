class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]]
        for _ in range(numRows-1):
            previous = result[-1]
            row =[1]
            for j in range(len(previous)-1):
                row.append(previous[j]+ previous[j+1])

            row.append(1)
            result.append(row)

        return result

        