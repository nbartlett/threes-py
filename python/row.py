
def combine(f, t):
    if f==0: 
        return t
    elif t==0: 
        return f
    elif ((f==1) and (t==2)) or ((f==2) and (t==1)): 
        return 3
    elif (f > 2) and (f == t):
        return f + t
    else:
        return -1

def canCombine(f, t):
    return combine(f, t) > -1

def merge(row, l, r):
    return row[:l] + [row[l] + row[r]] + row[(r+1):]

def copy(row):
    return [tile for tile in row]

def canShiftRight(row):
    for i in range(len(row) - 1, 0, -1):
        if canCombine(row[i-1], row[i]):
            return True
    return False

def shiftRight(row):
    newRow = copy(row);
    for i in range(len(newRow) - 1, 0, -1):
        if canCombine(newRow[i-1], newRow[i]):
            newRow = merge(newRow, i-1, i)
            newRow.insert(0, 0)
            return newRow
    return newRow

