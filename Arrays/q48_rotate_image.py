#48. Rotate Image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # horizontal reflection 
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]= matrix[i][n-j-1],matrix[i][j]    