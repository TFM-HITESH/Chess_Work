# Chess_Work

A simply repository I am using to play around with ideas in Chess Programming.


Encoding Algorithm : 


https://en.wikipedia.org/wiki/Board_representation_(computer_chess) 

A full description of a chess position, i.e. the position "state", must contain the following elements:

-The location of each piece on the board <br>
-Whose turn it is to move <br>
-Status of the 50-move draw rule. The name of this is sometimes a bit confusing, as it is 50 moves by each player, and therefore 100 half-moves, or ply. For example, if the previous 80 half-moves passed without a capture or a pawn move, the fifty-move rule will kick in after another twenty half-moves. <br>
-Whether either player is permanently disqualified to castle, both kingside and queenside. <br>
-If an en passant capture is possible. <br>


LOCATION (32 BYTES)

Using a Hexadecimal Character to represent each unit on a chessboard.

0 = Empty Square <br>

1 = White King = W.King ♔ <br>
2 = White Queen = W.Queen <br>
3 = White Rook = W.Rook <br>
4 = White Bishop = W.Bishop <br>
5 = White Knight = W.Knight <br>
6 = White Pawn = W.Pawn <br>

D = Empty Row = 00000000 <br>
E = Empty 4 squares = 0000 <br>
Precedence given to D then E then F <br>
F = nmF Next n squares are m. (only useful when number of spaces >= 3) <br>
Fg : 87F Next 8 squares are 7 (Black Pawn) <br>


7 = Black Pawn = B.Pawn <br>
8 = Black Knight = B.Knight <br>
9 = Black Bishop = B.Bishop <br>
A = Black Rook = B.Rook <br>
B = Black Queen = B.Queen <br>
C = Black King = B.King ♚ <br>


Regular Board : 

B.Rook B.Knight B.Bishop B.Queen B.King B.Bishop B.Knight B.Rook <br>
B.Pawn x 8  <br>
Empty <br>
Empty <br>
Empty <br>
Empty <br>
W.Pawn x 8 <br>
W.Rook W.Knight W.Bishop W.Queen W.King W.Bishop W.Knight W.Rook <br>

Encoded : <br>
A89BC98A <br>
87F <br>
D <br>
D <br>
D <br>
D <br>
86F <br>
35412453 <br>

pos = A89BC98A87FDDDD86F35412453 <br>
= A89BC98A77777777000000000000000000000000000000006666666635412453 (Max 32 Bytes) <br>
(Starting pos = 26 HEX = 104 bits = 13 Bytes) <br>

Maximum encoding = 8x8 = 64 Hexadecimal Chars. 1 hexadecimal = 2^4 or 4 bits. <br>
64 Hexadecimal = 64 x 4 = 256 bits = 32 Bytes. <br>

MOVE TURN AND CASTLING RIGHTS AND ENPASSANT ALLOWED WITH POSITION (1.5 BYTE) <br>

0000 0000 0000 - Convert to Hexadecimal <br>

1 - 0/1 Black/White Turn to play  <br>

2 - Black Kingside castle - 0/1 <br>
3 - Black Queenside castle - 0/1 <br>
4 - White Kingside castle - 0/1 <br>
5 - White Queenside castle - 0/1 <br>

6 - 0/1 En passant allowed if possible <br>

Following is only considered when 6th bit of previous information is 1 (Enpassant allowed) <br>

7 - 0/1 = Enpassant row for hexadecimal <br>
8 - 0/1 = Enpassant row for hexadecimal <br>
9 - 0/1 = Enpassant row for hexadecimal <br>
Rows 1 - 8 <br>

10 - 0/1 = Enpassant coloumn for hexadecimal <br>
11 - 0/1 = Enpassant coloumn for hexadecimal <br>
12 - 0/1 = Enpassant coloumn for hexadecimal <br>
Columns a - h <br>

Enpassant Row and Coloumn will only hold information <br>

Eg : <br>
1111 1000 0000  = F80 <br>
For starting position (White to play, no enpassant, all castling allowed) <br>
Converted to Hexadecimal <br>

50 MOVE DRAW (1 BYTE) <br>

0000 0000 - (Hexadecimal) <br>
  
0-256 - Stores 50 move draw information - 0-100 ply <br>
1 Byte <br>


Total = 32 + 1.5 + 1 = 34.5 Bytes (Worst Case Scenario) <br>

Total = LOCATION + MOVE TURN/ CASTLING RIGHT/ ENPASSANT ALLOWED - ENPASSANT INFO + 50 MOVE DRAW <br>

pos = A89BC98A87FDDDD86F35412453 F80 00 (Starting Position) <br>

Starting pos = 15.5 BYTES <br> 
Starting position using FEN : 56 BYTES <br>

Worst Case Scenario : 34.5 BYTES <br>
Worst Case Scenario FEN : 87 BYTES <br>
