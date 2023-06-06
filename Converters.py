import sys

class ConverterFuncs():

    #FEN > ARRAY  String input, Array Output COMPLETE
    def fenToArray(inFen):
    
        #start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        outArray = [] #output array

        mapDict = {'r':'bR','n':'bN','b':'bB','q':'bQ','k':'bK','p':'bp',
                   'R':'wR','N':'wN','B':'wB','Q':'wQ','K':'wK','P':'wp'}

        fenList = inFen.split("/")

        for row in fenList:
            outRow = [] #output row to be appended to outarray
            for col in row: #each individual character in fen
                if col.isdigit() is True :
                    for n in range(int(col)):
                        outRow.append("--") #appends -- n times
                else:
                    outRow.append(mapDict[col]) #appends from the map

            outArray.append(outRow)

        return outArray
    
    #ARRAY > FEN  Array Input, String Output COMPLETE
    def arrayToFen(inArray):
        '''
        inArray = [
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
        outStr = "" #str to hold final FEN
        outEStr = "" #str to hold FEN with E representing empty spaces
        mapDict = {'--':'E','bR':'r','bN':'n','bB':'b','bQ':'q','bK':'k','bp':'p',
                   'wR':'R','wN':'N','wB':'B','wQ':'Q','wK':'K','wp':'P'}
        emptyCount = 0 #to keep track of empty spaces

        for row in inArray:
            for piece in row:
                outEStr = outEStr + mapDict[piece]   
            outEStr = outEStr + '/' #adding the / at the end of each row str

        #to convert the empty spaces E to numbers
        for letter in outEStr:
            if letter != 'E':
                if emptyCount != 0: #when the letter is E and the empty space is not 0
                    outStr = outStr + str(emptyCount) #appends the no. of empty spaces
                    emptyCount = 0 #resets it to 0
                outStr = outStr + letter #adds the correct letter and moves on
            else:
                emptyCount = emptyCount + 1
        
        outStr = outStr[:-1] #removing the / at the end

        return outStr
    
    #HEX > ARRAY  Hex Input, Array Output COMPLETE
    def hexToArray(inHex):
        
        outArray = []

        mapDict = {'0':"--",'1':"wK",'2':"wQ",'3':"wR",'4':"wB",'5':"wN",'6':"wp",
                   '7':"bp",'8':"bN",'9':"bB",'A':"bR",'B':"bQ",'C':"bK"}

        #inHex = 0xA89BC98A87FDDDD86F35412453
        inHexDec = int(inHex) #converts to decimal
        
        #converter to string from int
        inHexStr = ""
        hexMap = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

        while inHexDec > 0:
            digit = inHexDec%16

            if digit>=10:
                inHexStr = inHexStr + hexMap[digit]
            else:
                inHexStr = inHexStr + str(digit)
            inHexDec = inHexDec//16
        inHexStr = inHexStr[::-1] #reversing it as by the above logic, it stores it backwards
        print(inHexStr) #inHexStr is converted string

        while True:
            outRow = []
            while len(outRow) != 8:
                
                pieceHex = inHexStr[-1]
                
                if pieceHex == 'D':
                    
                    outRow = ["--","--","--","--","--","--","--","--"]
                    inHexStr = inHexStr[:-1] #removing last character D
                    outArray.append(outRow)
                    outRow = [] #clearing it after inserting
                
                #implement E = 0000
                elif pieceHex == 'E':
                    for n in range(4):
                        outRow.append("--")
                    inHexStr = inHexStr[:-1]

                elif pieceHex == 'F':
                    inHexStr = inHexStr[:-1] #removing last character E

                    piece = mapDict[inHexStr[-1]] #pulls piece from map
                    n = int(inHexStr[-2:-1]) #number of times, between 1-8

                    while n>0: #appends piece, n times to outRow[]
                        outRow.append(piece)
                        n=n-1

                    inHexStr = inHexStr[:-2] # last 2 digits are removed

                else:
                    piece = mapDict[pieceHex] #pulling piece from mapping
                    
                    outRow.append(piece)
                    inHexStr = inHexStr[:-1] #last digit removed
                    

            outArray.append(outRow)          
            if len(outArray) == 8:
                break  
        outArray.reverse()

        return outArray
         
    #ARRAY > HEX  Array Input, Hex Output COMPLETE
    def arrayToHex(inArray):
        
        '''
        inArray = [
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

        outHexStr = ""
        outRows = []
        mapDict = {"--":'0',"wK":'1',"wQ":'2',"wR":'3',"wB":'4',"wN":'5',"wp":'6',
                   "bp":'7',"bN":'8',"bB":'9',"bR":'A',"bQ":'B',"bK":'C'}

        for row in inArray:
            outRow = ""
            for piece in row:
                outRow = outRow + mapDict[piece]
            outRows.append(outRow)

        #replacing '00000000' with 'D'
        for row in range(len(outRows)) :
            if outRows[row] == '00000000':
                outRows[row] = 'D'
            else: #to check 4 at a time - can be used for E and mnF
                for n in range(0,4):
                    tempRow = outRows[row]
                    tempRowList = list(tempRow) #taking tempRow as a list
                    tempStr = tempRowList[n:n+4] #creating a list to take it 4 at a time
                    if tempStr == list("0000"):
                        tempRowList[n:n+4] = 'E'
                        tempRowOut = "" #an output string that will store value of tempRowList updated to be put into outRows
                        for l in tempRowList:
                            tempRowOut = tempRowOut + l
                        outRows[row] = tempRowOut #replacing outRows with new tempRowOut string
                        break

        #n = 8 #default length of longest 
        for row in range(len(outRows)):
            if len(outRows[row]) <= 3:
                pass
            else:
                for n in range(8,3,-1): #starting checking from longest length to lowest length
                #check for nmF - next n pieces are m
                    tempRow = outRows[row]
                    tempRowList = list(tempRow)
                    for i in range(0,9-n):  #scans across the list n elements at a time
                        tempStr = tempRowList[i:i+n]
                        check = True
                        checkVar = tempStr[0]
                        for j in tempStr: #checking if all the elements in the list are the same
                            if checkVar == j:
                                continue
                            else: 
                                check = False #kills the loop as soon as one of them is wrong
                                break
                        
                        tempRowOut = ""
                        if check is True: #final updation of outRows loop
                            m = tempStr[0]
                            hexStr = str(n) + str(m) + 'F' #adds in nmF form
                            tempRowList[i:i+n] = hexStr
                            for l in tempRowList: #concatenates into a string
                                tempRowOut = tempRowOut + l
                            outRows[row] = tempRowOut #updates in outRow
                            break
                    if check is True: #leaves n loop
                        break
                      
        for row in outRows:
            outHexStr = outHexStr + row #concatenation of all list elements into single hexadecimal string
        
        outHex = hex(int(outHexStr,16))
        #to convert to hexadecimal number             
        return outHex

    #FEN > HEX String Input, Hex Output INCOMPLETE
    def fenToHex(inFen):
        pass

    #HEX > FEN Hex Input, String Output INCOMPLETE 
    def hexToFen(inHex):
        pass

#all commented ones are done (top3)

print(ConverterFuncs.arrayToHex([['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'], ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['--', '--', '--', '--', '--', '--', '--', '--'], ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'], ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']]))
#print(ConverterFuncs.hexToArray(0xA89BC98A87FDDDD86F35412453))
