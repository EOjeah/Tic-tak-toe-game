class StrictDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError("{} is not a legal key of this StricDict".format(repr(key)))
        dict.__setitem__(self, key, value)

class Error(Exception):
   """Base class for other exceptions"""
   pass

class PostionTakenError(Error):
   """Raised when the position is already taken"""
   pass

class InvalidCharacter(Error):
   """Raised when the icon is not X/O"""
   pass


def alternate():
    while True:
       yield 'player1'
       yield 'player2'

if __name__ == "__main__":

    players = StrictDict({'player1':None,'player2': None})

    game_status = StrictDict({i:' ' for i in range(9)})
    player1, player2 = None, None

    while True:
        try:
            player1 = str(input('Player1 X/O? '))
            if player1.lower() not in ['x','o']:
                raise InvalidCharacter
            break
        except InvalidCharacter:
            print("Oops!  Invalid character.  Try again...")
        except ValueError:
            print("Oops!  That was not valid.  Try again...")

    if player1 == 'x':
        player1 = 'X'
        player2 = 'O'
        players['player1'] = 'X'
        players['player2'] = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
        players['player1'] = 'O'
        players['player2'] = 'X'

    #After above e.g. player1 = X and player2 = O

    game_over = False

    # print(game_status)

    # pl.print_layout()

    # while not game_over:
    #     print()
    #     if game_status[0] is game_status[1] is game_status[2]:
    #         game_over = True

    # while True:
    #     try:
    #         play_position = int(input('Enter position: '))
    #         if play_position not in range(9):
    #             raise ValueError
    #         if game_status[play_position] is not None:
    #             raise PostionTakenError
    #         break
    #     except PostionTakenError:
    #         print("Oops!  That postion is taken.  Try again...")
    #     except Exception:
    #         print("Oops!  That was no valid postion.  Try again...")
    count = 0
    player_turn = alternate()
    while True:
        current_play = player_turn.__next__()
        print('{} turn, play'.format(current_play))
        #player one turn
        # print(game_status)
        game_positions = tuple(game_status.values())
        # print(game_positions)
        print('''
        | 0 | 1 | 2 |  |  | {0} | {1} | {2} | 
        -------------  |  -------------
        | 3 | 4 | 5 |  |  | {3} | {4} | {5} | 
        -------------  |  -------------
        | 6 | 7 | 8 |  |  | {6} | {7} | {8} |
        '''.format(*game_positions))
       
        if count >= 5 and count < 10:
            if game_positions[0] is not ' ' and (game_positions[0] is game_positions[1] is game_positions[2]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[0] is not ' ' and (game_positions[0] is game_positions[3] is game_positions[6]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[0] is not ' ' and (game_positions[0] is game_positions[4] is game_positions[8]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[1] is not ' ' and (game_positions[1] is game_positions[4] is game_positions[7]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[2] is not ' ' and (game_positions[2] is game_positions[5] is game_positions[8]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[2] is not ' ' and (game_positions[2] is game_positions[4] is game_positions[6]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[3] is not ' ' and (game_positions[3] is game_positions[4] is game_positions[5]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
            elif game_positions[6] is not ' ' and (game_positions[6] is game_positions[7] is game_positions[8]):
                print('Player {} Wins!'.format(players[player_turn.__next__()]))
                break
        elif count > 8:
            print('No Winner!')
            break

        while True:
            try:
                play_position = int(input('Enter position for {}: '.format(players[current_play])))
                if play_position not in range(9):
                    raise ValueError
                if game_status[play_position] is not ' ':
                    raise PostionTakenError
                break
            except PostionTakenError:
                print("Oops!  That postion is taken.  Try again...")
            except Exception:
                print("Oops!  That was no valid postion.  Try again...")
        count += 1
        #populate game_status 
        game_status[play_position] = players[current_play]

        #players = StrictDict({'player1':None,'player2': None})
        #current player = player1,
        #play_position = 4 and valid 
        print(game_status)

        # next_player = players[alternate.__next__()]
    

    #play_position is btw 0 and 8 that the user entered last
        

