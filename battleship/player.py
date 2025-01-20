from battleship.board import GameBoard
from copy import deepcopy


class Player:
    def __init__(self, name, game):
        self.name = name
        self.remaining = len(game.ships)

        self.placement = GameBoard(game.rows, game.cols)
        self.firing = GameBoard(game.rows, game.cols)
        self.ships = deepcopy(game.ships)


    def validate_coords(self, entry_prompt):
        # Check input validity
        coords = input(f'{entry_prompt}')
        coords = coords.split(' ')

        if len(coords) != 2:
            return [-1, -1]

        try:
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
        except ValueError:
            return [-1, -1]

        return coords


    def input_placement(self, ship, game):

        valid = False
        while valid is False:
            
            # Orientation validity
            valid_orientation = False
            while valid_orientation is False:

                entry_prompt = f'{self.name}, enter the orientation of your {ship.name}, which is {ship.length} long: '
                orientation = input(entry_prompt).lower()

                h = 'horizontally'
                v = 'vertically'

                for i in range(len(orientation)):

                    if orientation[i] == h[i]:
                        valid_orientation = True
                        continue

                    elif orientation[i] == v[i]:
                        valid_orientation = True
                        continue

                    else:
                        valid_orientation = False
                        break
                
                # Coordinate validity
                if valid_orientation is True:
                    ship.orientation = orientation[0]

                    entry_prompt = f'Enter the starting location for your {ship.name}, which is {ship.length} long, in the form row col: '
                    coords = self.validate_coords(entry_prompt)

                    if (0 <= coords[0] <= game.rows - 1) and (0 <= coords[1] <= game.cols - 1):
                        valid = self.placement.place_ship(ship, coords)

        print(f"{self.name}'s Placement Board")
        self.placement.draw_board()


    def input_fire(self, game):
        valid = False
        while valid is False:
            fcoords = [-1, -1]

            while not (0 <= fcoords[0] <= game.rows - 1) and not (0 <= fcoords[1] <= game.cols - 1):
                entry_prompt = f'{game.players[game.curr].name}, enter the location you want to fire at in the form row col: '
                fcoords = self.validate_coords(entry_prompt)

            valid = self.firing.fire(game, fcoords)
