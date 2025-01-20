from battleship.board import Ship
from battleship.player import Player


class GameState:
    def __init__(self, setup, player1, player2):
        
        # Board config
        self.rows = int(setup[0])
        self.cols = int(setup[1])
        self.ships = self.sort_ships(setup[2:])

        # Player config
        self.players = []
        self.players.append(Player(player1, self))
        self.players.append(Player(player2, self))

        # Current state
        self.curr_turn = 0
        self.curr = 0
        self.other = 1


    def sort_ships(self, ship_data):
        ships = {}
        ship_data.sort()

        for ship in ship_data:
            name, length = ship.split()
            ships[name] = (Ship(name, length))

        return ships


    def get_turn(self):
        self.curr_turn += 1
        self.curr = self.curr_turn % 2
        self.other = (self.curr_turn + 1) % 2


    def setup(self):
        for turn in range(2):

            curr = self.players[self.curr]

            print(f"{curr.name}'s Placement Board")
            curr.placement.draw_board()

            for ship in self.ships:
                curr.input_placement(self.ships[ship], self)

            self.get_turn()


    def play_turn(self):
        self.setup()

        while self.players[self.curr].remaining != 0 or self.players[self.other].remaining != 0:

            curr = self.players[self.curr]

            print(f"{curr.name}'s Placement Board")
            curr.placement.draw_board()

            print(f"{curr.name}'s Firing Board")
            curr.firing.draw_board()

            # Turn input
            curr.input_fire(self)
            self.check_destroyed_ship

            # Check for victory
            if curr.remaining == 0:
                print(f"{curr.name}'s Firing Board")
                curr.firing.draw_board()

                print(f"{curr.name}'s Placement Board")
                curr.placement.draw_board()

                print(f"{curr.name} won!")
                break

            self.get_turn()


    def check_destroyed_ship(self, name):

        curr = self.players[self.curr]
        other = self.players[self.other]

        # Check if rest of ship still exists
        for row in other.placement.board:
            for space in row:
                if space == name:
                    return

        other.ships[name].destroyed = True
        print(f"{curr.name} destroyed {other.name}'s {name}!")
        curr.remaining -= 1
