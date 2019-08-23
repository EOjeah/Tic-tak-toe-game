import print_layout as pl

def initialise_matrix():
    matrix = [[' ', ' ', ' '],[' ',' ', ' '],[' ', ' ', ' ']]
    # for i in range(0,3):
    #     for j in range(0,3):
    #         matrix[i][j] = ' '
    return(matrix)

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

def get_user_input(diction, value):
    return diction[value]

if __name__ == "__main__":
    matrix = initialise_matrix()
    game = create_game_dictionary()
    x = get_user_input(game, 9)
    print(x)
