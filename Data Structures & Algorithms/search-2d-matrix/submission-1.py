class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        st=0
        end=rows*cols-1
        while st<=end:
            mid=st+(end-st)//2
            row=mid//cols
            col=mid%cols
            if target > matrix[row][col]:
                st=mid+1
            elif target < matrix[row][col]:
                end=mid-1
            else:
                return True
        return False