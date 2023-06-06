    
import pygame as p
import ChessEngine

WIDTH = 512
HEIGHT = 512
#defining the size of the chessboard for the pygame command line as variables

DIMENSION = 8
#choosing dimension of the board as 8x8
SQ_SIZE = HEIGHT//DIMENSION
#size of each square

MAX_FPS = 15 
#capping the fps at 15 during animations

IMAGES = {}


#Creating a method to initialize a global dictionary of images. Make sure to do it only once in main as it is resource intensive

def loadImages():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']

    for piece in pieces:

        IMAGES[piece] = p.transform.scale(p.image.load("Pieces/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))

        #we have filled IMAGES dictionary with keys 'pieces' and values 'images'.
        #so IMAGES[piece] = Image of that piece

        #transform.scale will change the size of image to the dimensions sqsize x sqsize


#main running function
def main():

    p.init()
    #initializing pygame
    
    screen = p.display.set_mode((WIDTH,HEIGHT))
    #screen variable

    clock = p.time.Clock()
    #clock variable

    screen.fill(p.Color("white"))

    gs = ChessEngine.GameState()

    loadImages() #only doing this once b4 the while loop 

    running = True
    #run variable

    sqSelected = ()
    #saves selected square in a tuple
    #can be used for highlighting squares
    #holds last clicked square by user
    playerClicks = []
    #keeps track of player clicks, has 2 tuples, initial sq and final sq
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:

                location = p.mouse.get_pos() #tracks x,y of mouse location

                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE

                if sqSelected == (row,col): #user selects the previously selected square
                    sqSelected = () #unselecting the square
                    playerClicks = [] #removing player clicks
                    
                elif sqSelected != (row,col) :
                    sqSelected = (row,col) #row col info put into sqSelected
                    playerClicks.append(sqSelected) #adds upto 2 tuples for first and second clicks
                
                if len(playerClicks) == 2: #checks when 2 clicks have been made by user 
                    #now we want to make a move
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    #uses Move class
                    print(move.getChessNotation())

                    gs.makeMove(move) #finalises the move and does it

                    sqSelected = () #resets the user clicks to allow a second selection
                    
        
        

        clock.tick(MAX_FPS)
        p.display.flip()

        drawGameState(screen,gs)

        
#Responsible for all the graphics within current game state
def drawGameState(screen,gs):

    drawBoard(screen)
    #draws squares on the board

    drawPieces(screen,gs.board)
    #draws pieces on top of the squares


#draws squares on board. Top left square is always light, from both perspectives
def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    #list of colors

    for r in range(DIMENSION):
        for c in range(DIMENSION):

            color = colors[((r+c)%2)] 
            #even odd parity related to color, even is white, odd is black
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


#draws pieces on the squares using current gamestates board variable GameState.board
def drawPieces(screen,board):
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):

            piece = board[r][c]

            if piece != "--": #not empty
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

                

if __name__ == "__main__":
    main()

