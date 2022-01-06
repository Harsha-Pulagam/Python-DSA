class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
		Pay attention to how a two-dimensional list transforms after the clockwise rotation:
		[[1,2,3],[4,5,6],[7,8,9]]
		--------------------->
		[[7,4,1],[8,5,2],[9,6,3]]
		
		Before the matrix  is transformed, if we look at the list at index 2 ([7, 8, 9]), 
		these numbers have the respective indices of 0, 1, and 2. These indices are 
		important to note because when the list gets transformed, the indices of these
		numbers reveal which list they will appear inside in the transformed two-dimensional
		list. For example, at matrix[0][0], 7 appears. 7's index inside the original list was also 0. 
		Furthermore, at matrix[1][0], 8 appears, and at matrix[2][0], 9 appears. 8 had an 
		index of 1 in the original list, and 9 had an index of 2.
		
		It is also important to note that although these numbers appeared in the last list of
		the original matrix, these numbers (7, 8, and 9) appear at the start of every list in the
		transformed matrix. 
		
		This pattern is not unique to the last list of the original matrix. For example, if we look 
		at the list in the middle of the original matrix ([4, 5, 6]), these numbers will appear after
		7, 8, and 9 in their respective lists in the transformed matrix.
		
		With this pattern in mind, we can now iterate (backwards) through the matrix to append 
		the numbers in their appropriate places, and pop the numbers we are appending (so as to
		not duplicate numbers). We iterate through the list backwards because when we .append in
		python, the element comes at the end of the list... so for example, with regard to the 7 in the 
		last list of the original matrix, 7 will get appended at the end of the list [1, 2, 3]. When we 
		remove the duplicates, the numbers 1, 2, and 3 in this list will get popped, meaning that 7 
		will appear at the start of the list - and this is exactly what we want.
		"""
		
    length_matrix = len(matrix)

    for i in range(-1, -length_matrix -1, -1):
        for j in range(length_matrix):
            matrix[j].append(matrix[i][0])
            matrix[i].pop(0)
                
              
              
                
                
                
