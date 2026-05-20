class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        left, right = 0, len(matrix[0])-1


        while left < right:       
                for c in range(right - left):
                    top, bottom = left, right
                    top_left = matrix[top][left+c]
                    matrix[top][left+c] = matrix[bottom-c][left]

                    #move bottom right into bottom left
                    matrix[bottom-c][left] = matrix[bottom][right-c]

                    #move top right into bottom right
                    matrix[bottom][right-c] = matrix[top+c][right]

                    matrix[top + c][right] = top_left

                right -=1
                left +=1





        