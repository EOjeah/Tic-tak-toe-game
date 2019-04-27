
def create_game_dictionary():
    """
    Creates the game mapping 
    """
    GAME = {}
    x = 0
    for i in reversed(range(0,3)):
        for j in range(0,3):
            x+=1
            temp = []
            temp.append(i)
            temp.append(j)
            GAME[x] = temp

    return GAME
    

