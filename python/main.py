import grid
import math
import random

def takeTiles(mx):
    'get a list of tiles that are all least than the supplied max (mx)'
    tiles = [1,2,3]
    while (2 * tiles[-1]) < mx:
        tiles.append(2 * tiles[-1])
    return tiles

class Game:
    def __init__(self, grid, stack = [], rng = None): 
        self.grid = grid
        self.stack = stack
        self.rng = rng
        if (rng is None):
            self.rng = random.Random(3)

    def _resetStack(self):
        stack = [1] * 4 + [2] * 4 + [3] * 4
        mx = grid.max(self.grid)
        if (mx > 48) and self.rng.random() < 0.5:
            tiles = takeTiles(mx / 6)[2:]
            stack.append(tiles[int(self.rng.random() * len(tiles))])
        self.rng.shuffle(stack)
        self.stack = stack

    def _resetStackCheck(self):
        if len(self.stack) < 1:
            self._resetStack()

    def _nextTile(self):
        self._resetStackCheck()
        return self.stack.pop()

    def whatIsNextTile():
        self._resetStackCheck()
        if (self.stack[-1] == 1) or (self.stack[-1] == 2):
            return self.stack[-1]
        else:
            return -1

    def canShiftRight(self):
        return grid.canShiftRight(self.grid)

    def canShiftLeft(self):
        return grid.canShiftLeft(self.grid)

    def canShiftUp(self):
        return grid.canShiftUp(self.grid)

    def canShiftDown(self):
        return grid.canShiftDown(self.grid)

    def shiftRight(self):
        if grid.canShiftRight(self.grid):
            return Game(grid.shiftRight(self.grid, self.rng.random(), self._nextTile()), self.stack, self.rng)
        else:
            return Game(grid.copy(self.grid), self.stack, self.rng)

    def shiftLeft(self):
        if grid.canShiftLeft(self.grid):
            return Game(grid.shiftLeft(self.grid, self.rng.random(), self._nextTile()), self.stack, self.rng)
        else:
            return Game(grid.copy(self.grid), self.stack, self.rng)

    def shiftUp(self):
        if grid.canShiftUp(self.grid):
            return Game(grid.shiftUp(self.grid, self.rng.random(), self._nextTile()), self.stack, self.rng)
        else:
            return Game(grid.copy(self.grid), self.stack, self.rng)

    def shiftDown(self):
        if grid.canShiftDown(self.grid):
            return Game(grid.shiftDown(self.grid, self.rng.random(), self._nextTile()), self.stack, self.rng)
        else:
            return Game(grid.copy(self.grid), self.stack, self.rng)

    def score(self):
        return grid.score(self.grid)

    def done(self):
        return grid.done(self.grid)

    def __str__(self):
        return '\n'.join([str(r) for r in self.grid])

    def __repr__(self):
        return self.__str__()


