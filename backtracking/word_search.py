class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        
        n=len(board)
        m=len(board[0])
        
        for i in range(n):
            for j in range(m):
                if self.found(word, board, i, j):
                    return True
        return False
        
    def found(self, word, board, i, j):
        
        if word[0]==board[i][j]:
            if not word[1:]:
                return True
            board[i][j]=" "
            
            if i<len(board)-1 and self.found(word[1:],board, i+1,j):
                return True
            if i>0 and self.found(word[1:],board, i-1,j):
                return True
            if j<len(board[0])-1 and self.found(word[1:],board, i,j+1):
                return True
            if j>0 and self.found(word[1:],board, i,j-1):
                return True
            board[i][j]=word[0]
            return False
        else: 
            return False
            
        