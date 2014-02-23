import row
import math

def copy(grid):
    return [row.copy(r) for r in grid]

def scoreTile(tile):
    if tile < 3:
        return 0
    else:
        return 3**(int(math.log(tile / 3, 2)) + 1)

def reverseRows(grid):
    g = []
    for r in grid:
        newRow = row.copy(r)
        newRow.reverse()
        g.append(newRow)
    return g

def transpose(grid):
    g = [[] for r in grid]
    for r in grid:
        for i, tile in enumerate(r):
            g[i].append(tile)
    return g

def score(grid):
    s = 0
    for r in grid:
        for tile in r:
            s += scoreTile(tile)
    return s

def canShiftRight(grid): 
    for r in grid:
        if row.canShiftRight(r):
            return True
    return False

def shiftRight(grid, rnd, value):
    g = []
    idxs = []
    for idx, r in enumerate(grid):
        if row.canShiftRight(r):
            idxs.append(idx)
            g.append(row.shiftRight(r))
        else:
            g.append(row.copy(r))

    if len(idxs) > 0:
        g[idxs[int(rnd * len(idxs))]][0] = value

    return g

def canShiftLeft(grid): 
    return canShiftRight(reverseRows(grid))

def shiftLeft(grid, rnd, value): 
    return reverseRows(shiftRight(reverseRows(grid), rnd, value))

def canShiftUp(grid): 
    return canShiftLeft(transpose(grid))

def shiftUp(grid, rnd, value):
    return transpose(shiftLeft(transpose(grid), rnd, value))

def canShiftDown(grid): 
    return canShiftRight(transpose(grid))

def shiftDown(grid, rnd, value):
    return transpose(shiftRight(transpose(grid), rnd, value))

def max(grid):
    mx = 0
    for r in grid:
        for tile in r:
            if tile > mx:
                mx = tile
    return mx

def done(grid):
    return not (canShiftRight(grid) or canShiftLeft(grid) or canShiftDown(grid) or canShiftUp(grid))
