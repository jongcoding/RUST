import sys

input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

# 비트마스크로 각 행/열/박스의 사용 숫자 추적
row_mask = [0] * 9
col_mask = [0] * 9
box_mask = [0] * 9
empty = []

def box_idx(r, c):
    return (r // 3) * 3 + (c // 3)

for r in range(9):
    for c in range(9):
        val = board[r][c]
        if val == 0:
            empty.append((r, c))
        else:
            bit = 1 << val
            row_mask[r] |= bit
            col_mask[c] |= bit
            box_mask[box_idx(r, c)] |= bit

def dfs(idx):
    if idx == len(empty):
        return True
    r, c = empty[idx]
    b = box_idx(r, c)
    used = row_mask[r] | col_mask[c] | box_mask[b]
    for v in range(1, 10):  # 작은 수부터 채워 사전순 최소
        bit = 1 << v
        if used & bit:
            continue
        board[r][c] = v
        row_mask[r] |= bit
        col_mask[c] |= bit
        box_mask[b] |= bit
        if dfs(idx + 1):
            return True
        # backtrack
        board[r][c] = 0
        row_mask[r] &= ~bit
        col_mask[c] &= ~bit
        box_mask[b] &= ~bit
    return False

dfs(0)

for r in range(9):
    print(''.join(map(str, board[r])))
