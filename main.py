from battleship.gamestate import GameState


def get_players():
    player1_name = input('Player 1, please enter your name: ')
    player2_name = input('Player 2, please enter your name: ')

    return player1_name, player2_name


def main():
    board_configuration_path = input('Please enter the path to the configuration file for this game: ')

    setup_values = []

    with open(board_configuration_path) as board_configuration_file:
        for line in board_configuration_file:
            setup_values.append(line)

    for i in range(len(setup_values)):
        setup_values[i] = setup_values[i].strip('\n')

    player1_name, player2_name = get_players()

    game = GameState(setup_values, player1_name, player2_name)
    game.play_turn()


main()
