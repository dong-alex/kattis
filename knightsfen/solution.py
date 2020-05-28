tests = int(input())
completeBoard = [['1', '1', '1', '1', '1'], ['0', '1', '1', '1', '1'], [
    '0', '0', ' ', '1', '1'], ['0', '0', '0', '0', '1'], ['0', '0', '0', '0', '0']]

# all the potential directions a knight can come from (2, 1)
directions = [(2, 1), (2, -1), (-2, 1),
              (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

# if the board is not complete - return false - otherwise return true


def isSolved():
    for i in range(5):
        for j in range(5):
            if board[i][j] != completeBoard[i][j]:
                return False
    return True


def isValid(x, y, i, j):
    # don't take the same space where it was - that would be going back to the same spot where we don't need to
    return (0 <= x < 5 and 0 <= y < 5) and not (x == i and y == j)


def dfs(i, j, oldX, oldY, depth):
    # if we go beyond 10 depth - not possible
    if depth > 10:
        return 100

    # base case - solved board requires no further iterations
    if isSolved():
        return 0
    # check for valid positioning
    # get minimum depth required
    temp = 100
    for d in directions:
        newX = i + d[0]
        newY = j + d[1]

        # backtracking algorithm
        if isValid(newX, newY, oldX, oldY):
            # swap the position of the board
            board[i][j], board[newX][newY] = board[newX][newY], board[i][j]
            # use new depth and track it
            temp = min(temp, 1 + dfs(newX, newY, i, j, depth + 1))
            # swap back the board for the next position
            board[i][j], board[newX][newY] = board[newX][newY], board[i][j]
    # return the minimum depth - 100 if its not possible
    return temp


while tests:
    board = []

    # read the board
    for i in range(5):
        board.append(list(input().strip('\n')))

    # find the empty space we can branch from
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                x = i
                y = j
                break

    d = dfs(x, y, x, y, 0)
    if d > 10:
        print("Unsolvable in less than 11 move(s).")
    else:
        print("Solvable in", d, "move(s).")
    tests -= 1
