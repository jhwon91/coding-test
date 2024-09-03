class Solution(object):
	def maximalRectangle(self, matrix):
		temp = [0] * len(matrix[0])
		print(temp)

		for row in matrix:
			for col in row:
				if col == "1":
					print(row,col)



matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solution = Solution()
# Call the maximalRectangle method
max_area = solution.maximalRectangle(matrix)