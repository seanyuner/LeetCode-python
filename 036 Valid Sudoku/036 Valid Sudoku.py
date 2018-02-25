# 103ms 22.17%
class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            a = []
            for i in range(9):
                if board[row][i] != '.':
                    a.append(board[row][i])
                if len(a) != len(set(a)):
                    return False
        for col in range(9):
            a = []
            for i in range(9):
                if board[i][col] != '.':
                    a.append(board[i][col])
                if len(a) != len(set(a)):
                    return False
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                a = []
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if board[i+k][j+l] != '.':
                            a.append(board[i+k][j+l])
                        if len(a) != len(set(a)):
                            return False        
        return True


# 73ms 75.92%
class Solution2(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            a = {}
            for i in range(9):
                if board[row][i] != '.':
                    if board[row][i] in a:
                        return False
                    a[board[row][i]] = 1
        for col in range(9):
            a = {}
            for i in range(9):
                if board[i][col] != '.':
                    if board[i][col] in a:
                        return False
                    a[board[i][col]] = 1
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                a = {}
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if board[i+k][j+l] != '.':
                            if board[i+k][j+l] in a:
                                return False
                            a[board[i+k][j+l]] = 1       
        return True


# 70ms 84.86%
class Solution3(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hash_row = {}
        hash_col = {}
        hash_squ = {}
        for i in range(9):
            hash_row[i] = {}
            hash_col[i] = {}
            hash_squ[i] = {}
        """
        # 69ms 84.86%
        hash_row = [{} for _ in range(9)]
        hash_col = [{} for _ in range(9)]
        hash_squ = [{} for _ in range(9)]
        """

        for i in range(9):
            for j in range(9):
                key = board[i][j]
                if key == '.': continue
                squ = 3*(i/3)+j/3
                if key in hash_row[i] or key in hash_col[j] or key in hash_squ[squ]:
                    return False
                hash_row[i][key] = True
                hash_col[j][key] = True
                hash_squ[squ][key] = True
        return True


# 73ms 75.92%
class Solution4(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.is_row_valid(board) and self.is_col_valid(board)\
               and self.is_squ_valid(board)
    
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
        
    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
        
    def is_squ_valid(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = []
                for k in [0, 1, 2]:
                    for l in [0, 1, 2]:
                        square.append(board[i + k][j + l])
                if not self.is_unit_valid(square):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        a = {}
        for i in unit:
            if i == '.': continue
            if i in a:
                return False
            a[i] = True
        return True
