#initialize empty board
empty_board = [None, None, None, None, None, None, None, None, None]

PLAYER_1 = "X"
PLAYER_2 = "X"

a_board = ["X", None, None, None, "X", None, None, "O", None]

#draw board
def new_board():
    return empty_board

## | X |   |   |
## | O | X |   |
## |   |   | O |

#testing something ignore this
#print(f"| {empty_board[0] if empty_board[0] else '   '} | {empty_board[1] if empty_board[1] else ' '} | {empty_board[2] if empty_board[2] else '  '}|")
def draw_board(board):
    draw = "\n"+" --- --- ---" +"\n"
    
    for i in range(len(board)):
        if i%3 == 0:
          draw += "|"

        if board[i] == "O":
            draw += " O |"
        elif board[i] == "X":
            draw += " X |"
        else:
          #  draw += "   |"
          draw += " " + str(i+1) + " |"
        
        if i%3 == 2:
          draw += "\n"+" --- --- ---" +"\n"

    return draw

#print(draw_board(empty_board))

#define game loop
#   while game is not over continue

#   select a square to make your move
#   redraw board
#   check if winning move
#   else
#   change turn to next player

#   if winning move end game, congratulate winnder


#define how turns will be played

#getting player input
def get_move(board):
  
  print("Hello Player 2(O's), please Choose your move on an Empty square: ")
  print(draw_board(board))
  player_move = int(input("Enter a number of where you would like to play: "))
  
  return int(player_move)



#check if move is valid

#make move
def make_move(move, board, player):
  move = move_valid(move, board)
  if player == PLAYER_1:
     board[move-1] = "X"
  else:
     board[move-1] = "O"

  return board

def move_valid(move, board):
    is_valid = False
    while is_valid is False:
      is_valid = True
      if move < 1 or move > 9:
        print("Invalid move! Please enter a new one")
        move = int(input("Enter a number of where you would like to play: "))
        is_valid = False
      elif board[move-1]:
        print(f"This spot is taken by {board[move-1]}, please choose a new one!")
        move = int(input("Enter a number of where you would like to play: "))
        is_valid = False

    return move

   
   
make_move(get_move(a_board), a_board, PLAYER_1)
print(draw_board(a_board))

#define how to calculate if a win or a draw has been played


