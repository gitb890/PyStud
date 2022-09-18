class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False
        num_row = len(array)
        num_col = len(array[0])
        i,j = 0, num_col-1
        while j >= 0 and i < num_row:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True



# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         i, j = len(matrix) - 1, 0
#         while i >= 0 and j < len(matrix[0]):
#             if matrix[i][j] > target: i -= 1
#             elif matrix[i][j] < target: j += 1
#             else: return True
#         return False