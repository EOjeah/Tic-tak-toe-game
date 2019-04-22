
def get_player_details():
    player_one = {'name':None, 'character':None, 'win':False}
    player_two = {'name':None, 'character':None, 'win':False}

    player_one['name'] = input("Enter Player 1 name: ")
    player_one['name'] = player_one['name'].capitalize()
    
    print("Player 1's name is {}".format(player_one['name']))
    
    while True:
        player_one['character'] = input("Enter Player 1's character X/O: ")
        if  not (player_one['character'].lower() == 'x' or player_one['character'].lower() == 'o'):
            print("Invalid char, please type in X or O")
            continue
        break
    print("Player 1's character is {}".format(player_one['character'].upper()))
    player_one['character'] = player_one['character'].upper()

    player_two['name'] = input("Enter Player 2 name: ")
    player_two['name'] = player_two['name'].capitalize()
    player_two['character'] = 'X' if player_one['character'] == 'O' else 'O'
    print("Player 2's character is {}".format(player_two['character']))

get_player_details()