class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[0])-1]:
                print(i)
                l = 0
                m = len(matrix[0])-1
                while l<=m:
                    print(l,m)
                    mid = (l+m)//2
                    if matrix[i][mid] == target:
                        return True
                    else:
                        if matrix[i][mid] > target:
                            m = mid - 1
                        else:
                            l = mid + 1
        return False

                