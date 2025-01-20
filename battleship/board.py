class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = int(length)
        self.destroyed = False
        self.orientation = '0'


class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []

        for row in range(self.rows):
            self.board.append([])

            for col in range(self.cols):
                self.board[row].append('*')

    def draw_board(self):

        print('  ', end='')

        # Print column labels
        for col_num in range(self.cols):
            print(col_num, end=' ')

        print()

        for row in range(self.rows):
            # Print row labels
            print(row, end='')

            # Print board spaces
            for space in range(self.cols):

                if space != self.cols - 1:
                    print(f' {self.board[row][space]}', end='')
                else:
                    print(f' {self.board[row][space]}')

    def place_ship(self, ship, coords):
        first_row = coords[0]
        first_col = coords[1]

        # Check if ship fits on board
        if ship.orientation == 'h':
            last_row = first_row
            last_col = first_col + ship.length - 1

        elif ship.orientation == 'v':
            last_row = first_row + ship.length - 1
            last_col = first_col

        if last_row >= self.rows or last_col >= self.cols:
            return False

        # Place ship if nothing is blocking placement
        if ship.orientation == 'h':

            # Check if anything is blocking placement
            for i in range(ship.length):
                if self.board[coords[0]][coords[1] + i] != '*':
                    return False

            # Place ship
            for i in range(ship.length):
                self.board[coords[0]][coords[1] + i] = ship.name

        elif ship.orientation == 'v':

            # Check if anything is blocking placement
            for i in range(ship.length):
                if self.board[coords[0] + i][coords[1]] != '*':
                    return False

            # Place ship
            for i in range(ship.length):
                self.board[coords[0] + i][coords[1]] = ship.name

        return True

    def fire(self, game, fcoords):

        if (fcoords[0] >= self.rows) or (fcoords[1] >= self.cols):
            return False

        # Set players and firing position
        curr = game.players[game.curr]
        other = game.players[game.other]
        pos = other.placement.board[fcoords[0]][fcoords[1]]

        if pos != '*':

            # If firing position has already been hit before
            if pos == 'X' or pos == 'O':
                return False

            else:
                print(f"{curr.name} hit {other.name}'s {pos}!")

                # Update boards
                other.placement.board[fcoords[0]][fcoords[1]] = 'X'
                self.board[fcoords[0]][fcoords[1]] = 'X'

                game.check_destroyed_ship(pos)

        else:
            print(f"{curr.name} missed.")

            # Update boards
            other.placement.board[fcoords[0]][fcoords[1]] = 'O'
            self.board[fcoords[0]][fcoords[1]] = 'O'

        return True


g = GameBoard(8, 8)
g.draw_board()