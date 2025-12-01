import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())
board0 = [list(map(int, input().split())) for _ in range(N)]


def compress_merge(line, reverse=False):

    if reverse:
        line = line[::-1]
    nums = [x for x in line if x != 0]

    merged = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            merged.append(nums[i] * 2)
            i += 2
        else:
            merged.append(nums[i])
            i += 1

    merged += [0] * (len(line) - len(merged))
    if reverse:
        merged.reverse()
    return merged


def move(board, direction):
    """direction: 0=up, 1=down, 2=left, 3=right"""
    new_board = [row[:] for row in board]
    if direction == 0:  # up
        for c in range(N):
            col = [new_board[r][c] for r in range(N)]
            col_new = compress_merge(col, reverse=False)
            for r in range(N):
                new_board[r][c] = col_new[r]
    elif direction == 1:  # down
        for c in range(N):
            col = [new_board[r][c] for r in range(N)]
            col_new = compress_merge(col, reverse=True)
            for r in range(N):
                new_board[r][c] = col_new[r]
    elif direction == 2:  # left
        for r in range(N):
            new_board[r] = compress_merge(new_board[r], reverse=False)
    else:  # right
        for r in range(N):
            new_board[r] = compress_merge(new_board[r], reverse=True)
    return new_board


def max_tile(board):
    return max(max(row) for row in board)


answer = max_tile(board0)


def dfs(depth, board):
    global answer
    if depth == 5:
        return
    for d in range(4):
        nxt = move(board, d)
        if nxt == board:
            continue
        answer = max(answer, max_tile(nxt))
        dfs(depth + 1, nxt)


dfs(0, board0)
print(answer)
