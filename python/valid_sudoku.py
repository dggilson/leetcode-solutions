class Solution(object): 
 def isValidSudoku(self, board):
        i = 0
        j = 0
        value_set = set()
        for i in range(9):
            value_set.clear()
            for j in range(9):
            #checks if each value in the row is unique
                if board[i][j] != ".":
                    before_len = len(value_set)
                    value_set.add(board[i][j])
                    if before_len == len(value_set):
                        return False
        for j in range(9):
            value_set.clear()
            for i in range(9):
            #check if each value in the column is unique
                if board[i][j] != ".":
                    before_len = len(value_set)
                    value_set.add(board[i][j])
                    if before_len == len(value_set):
                        return False
        end_row = 3
        end_column = 3
        start_row = 0
        start_column = 0
        cnt = 0
        indx = [0,3,6]
        for i in range(9):
            value_set.clear()
            #updates the row and col indices start_row by iterating between 0, 3, 6
            start_row = indx[i%3]
            end_row = start_row+3
            #after we shift between all the rows in the first column we jump to the 2nd row
            # X _ _
            # X _ _
            # X _ _
            if(start_row == 0):
                start_column = indx[cnt]
                end_column = start_column + 3
                cnt += 1
            for j in range(start_row, end_row):
                for k in range(start_column, end_column):
                #check if each value in 3x3 is unique
                    if board[j][k] != ".":
                        before_len = len(value_set)
                        value_set.add(board[j][k])
                        if before_len == len(value_set):
                            return False
        return True