
import random
test_board = ['X', None, None,
             None, 'O', 'O',
             'X', None, None]

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