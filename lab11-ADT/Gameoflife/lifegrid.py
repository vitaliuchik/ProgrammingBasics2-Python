from arrays import Array2D

class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid. 
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        
        :param coord_list: 
        :return: 
        """
        self._grid.clear(0)
        for coord in coord_list:
            self.set_cell(coord[0], coord[1])


    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?
        
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return self._grid[row, col] == 1

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 0


    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = 1       


    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return: 
        """
        count = 0
        for row_pos in range(row-1, row+2):
            for col_pos in range(col-1, col+2):
                if row_pos == row and col_pos == col:
                    continue
                else:
                    try:
                        count += self._grid[row_pos, col_pos]
                    except AssertionError:
                        pass
        return count

