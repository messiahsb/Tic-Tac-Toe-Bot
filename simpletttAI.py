
import random
test_board = [None, None, 'O',
            None, 'X', None,
             'X', 'O', "O"]

def randommove_ai(board, player):
    out = []
    for i in range(len(board)):
     if not board[i]:
      out.append(i+1)
    return random.choice(out)


def winningpos_ai(board, player):
    if player:
     play = "O"
    else:
     play = "X"

    win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                [0, 4, 8], [2, 4, 6]]

    for a, b, c in win_states:
            if play == [a] == board[b] and not board[c]:
               return c+1
            elif play == board[a] == board[c] and not board[b]:
               return b+1
            elif play == board[b] == board[c] and not board[a]:
               return a+1
           
    return randommove_ai(board, player)

def winning_and_losingpos_ai(board, player):
    if player:
     play1 = "O"
     play2 = "X"
    else:
     play1 = "X"
     play2 = "O"

    win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                [0, 4, 8], [2, 4, 6]]

    for a, b, c in win_states:
            if play1 == [a] == board[b] and not board[c]:
               return c+1
            elif play1 == board[a] == board[c] and not board[b]:
               return b+1
            elif play1 == board[b] == board[c] and not board[a]:
               return a+1
            elif play2 == board[a] == board[b] and not board[c]:
               return c+1
            elif play2 == board[a] == board[c] and not board[b]:
               return b+1
            elif play2 == board[b] == board[c] and not board[a]:
               return a+1
            
    return randommove_ai(board, player)

def human_player(board, player):
    # print(draw_board(board))
  print(f"Player {player +1} please make your move!")
  try:
    player_move = int(input("Enter a number of where you would like to play: "))
  except ValueError as e:
    print("Entered Character was not a number try again: ")
    player_move = human_player(board, player)

  
  return int(player_move)


  


def check_winner(board):
  win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                [0, 4, 8], [2, 4, 6]]
  for a, b, c in win_states:
    if board[a] and board[a] == board[b] == board[c]:
      return board[a]
  return None

def make_move(move, board, player):
  # can move this into the main loop after initialization
  # while not move_valid(move, board):
  #    move = get_move(board)
  if player:
     board[move] = "O"
  else:
     board[move] = "X"

  return board

# For simplicity we'll assume that our AI
# always plays as X.
#
# "X" for Xpert!
# "O" for Opponent!
#
# `board` is a 2-D grid of the state to be scored
# `current_player` is the player whose turn it is
#   ('X' or 'O')

#I CAN OPTIMIZE THIS USING MEMOIZATION, INCLUDE THE LEGAL LIST MOVE IN FUNCTION DEF
def minimax_score(board, current_player, who_am_i):
   if who_am_i:
      player = 'O' 
   else:
      player = 'X'

   if all(board):
      if check_winner(board) is None:
         return 0
      elif check_winner(board) == player:
         return 10
      elif check_winner(board) != player:
         return -10
      
   legal_moves = [i for i,n in enumerate(board) if n is None]

   scores = []
   for move in legal_moves:
      _board = board.copy()
      new_board = make_move(move, _board, current_player)
      scores.append(minimax_score(new_board, current_player^1, who_am_i))

   if not current_player:
      return max(scores)
   else:
      return min(scores)
   
   #scores.append(minimax_score(new_board, current_player^1))

def minimax_ai(board, current_player, who_am_i):

   legal_moves = [i for i,n in enumerate(board) if n is None]
   scores = {}
   for move in legal_moves:
      _board = board.copy()
      new_board = make_move(move, _board, current_player)
      scores[move] = minimax_score(new_board, current_player^1, who_am_i)
   return max(scores, key=scores.get) +1
   
empty_board = [None, None, None, None, None, None, None, None, None]

