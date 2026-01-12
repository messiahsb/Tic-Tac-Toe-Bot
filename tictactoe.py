#initialize empty board
empty_board = [None, None, None, None, None, None, None, None, None]

PLAYER_1 = 0
PLAYER_2 = 1

a_board = ["X", None, None, None, "X", None, None, "O", None]

#draw board
def new_board():
    return empty_board

## | 1 | 2 | 3 |
## | 4 | 5 | 6 |
## | 7 | 8 | 9 |

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

#define game loop

def game_loop():
  game_board = empty_board
  print(draw_board(game_board))
  current_player = 0b0

  #   while game is not over continue
  while True:
    print(f"Player {current_player +1} please make your move!")

    #   select a square to make your move
    move = get_move()
    while not move_valid(move, game_board):
      move = get_move()

    #   redraw board
    game_board = make_move(move, game_board, current_player)
    print(draw_board(game_board))
    
#   check if winning move
#   else
#   change turn to next player
    current_player^=1


#   if winning move end game, congratulate winnder
## | 1 | 2 | 3 |
## | 4 | 5 | 6 |
## | 7 | 8 | 9 |
test_board = ["X", "O", "X",
               "O", "X", "O", 
               "O", "X", "O"]

def check_winner(board):
  win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                [0, 4, 8], [2, 4, 6]]
  for a, b, c in win_states:
    if board[a] and board[a] == board[b] == board[c]:
      return board[a]
  
  return None

print(check_winner(test_board))
#define how turns will be played

#getting player input
def get_move():
  
  #MOVE THESE TOO LINE TO THE MAIN LOOP FUNTION WHEN CONSTRUCTED, PRINT AT THE CHANGE OF A TURN
  # print("Hello Player 2(O's), please Choose your move on an Empty square: ")
  # print(draw_board(board))
  player_move = int(input("Enter a number of where you would like to play: "))
  
  return int(player_move)



#check if move is valid
def move_valid(move, board):
    #changed some of the logic to loop in make move, this function now purely checks validity
   # while is_valid is False:

    is_valid = True
    if move < 1 or move > 9:
      print("Invalid move! Please enter a new one")
      # move = int(input("Enter a number of where you would like to play: "))
      is_valid = False
    elif board[move-1]:
      print(f"This spot is taken by {board[move-1]}, please choose a new one!")
      #move = int(input("Enter a number of where you would like to play: "))
      is_valid = False
    #add statement to check if is integer
    return is_valid

#make move
def make_move(move, board, player):

  # can move this into the main loop after initialization
  # while not move_valid(move, board):
  #    move = get_move(board)

  if player:
     board[move-1] = "O"
  else:
     board[move-1] = "X"

  return board

   
# make_move(get_move(a_board), a_board, PLAYER_1)
# print(draw_board(a_board))
#game_loop()

#define how to calculate if a win or a draw has been played


