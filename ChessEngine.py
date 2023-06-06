import Converters

class GameState():
    def __init__(self):

        '''
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        '''
        
        self.board = Converters.ConverterFuncs.fenToArray("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

        #first char represents black or white b/w
        #second char represents piece K,Q,B,R,N,p
        #-- means blank

        self.whiteToMove = True

        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--" #sets the previous sqaure to empty piece
        self.board[move.endRow][move.endCol] = move.pieceMoved #sets new square to piece that is moved

        self.moveLog.append(move) #logging the moves for undoing later/ displaying history 
        self.whiteToMove = not self.whiteToMove #swaps turn to move

class Move():

    #creating dictionary maps to map computer notation to chess notation

    ranksToRows = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
    rowsToRanks = {v:k for k,v in ranksToRows.items()}    

    filesToCols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    colsToFiles = {v:k for k,v in filesToCols.items()} 

    def __init__(self, startSq, endSq, board):

        self.startRow = startSq[0]
        self.startCol = startSq[1]

        self.endRow = endSq[0]
        self.endCol = endSq[1]

        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    
    def getChessNotation(self):
        #we can add to this notation to make it realistic chess notation with x,+,# etc.
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        #returns a string of first and last position
    
    '''
    def getChessNotation(self):
        chessdict = {'bR':'R', 'wR':'R', 'bB':'B', 'wB':'B', 'bN':'N', 'wN':'N', 'bQ':'Q', 'wQ':'Q', 'wK':'K', 'bK':'K'}
        notation = ''
        if self.pieceCaptured == '--' and (self.pieceMoved != 'wp' and self.pieceMoved != 'bp'):
            ans = chessdict[self.pieceMoved]
            notation = ans + self.getRankFile(self.endRow, self.endCol)
        elif self.pieceCaptured == '--' and (self.pieceMoved == 'wp' or self.pieceMoved == 'bp'):
            notation = self.getRankFile(self.endRow, self.endCol) 
        elif self.pieceCaptured != '--':
            if self.pieceMoved != 'wp' and self.pieceMoved != 'bp':
                ans = chessdict[self.pieceMoved]
                notation = ans + 'x' + self.getRankFile(self.endRow, self.endCol)
            else:
                notation = self.pieceMoved + 'x' + self.getRankFile(self.endRow, self.endCol)
        return notation
    '''
    
    def getRankFile(self, r, c): #helper function
        return self.colsToFiles[c] + self.rowsToRanks[r]
        #returns a string of r and c converted to chess notation
