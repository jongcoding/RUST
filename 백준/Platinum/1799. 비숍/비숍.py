import sys

# 체스판의 크기 10 이하

input = sys.stdin.readline


def main():
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]

    # 비숍은 색이 다른 칸을 서로 공격할 수 없으므로 색을 나눠 탐색
    cells_per_color = [[], []]
    for r in range(size):
        for c in range(size):
            if board[r][c] == 1:
                cells_per_color[(r + c) % 2].append((r, c))

    def max_bishops(cells):
        diag_ltr = [False] * (2 * size)  # ↘ 대각선
        diag_rtl = [False] * (2 * size)  # ↙ 대각선
        best = 0

        def dfs(idx, count):
            nonlocal best
            if idx == len(cells):
                if count > best:
                    best = count
                return

            r, c = cells[idx]
            d1 = r + c
            d2 = r - c + size - 1

            if not diag_ltr[d1] and not diag_rtl[d2]:
                diag_ltr[d1] = diag_rtl[d2] = True
                dfs(idx + 1, count + 1)
                diag_ltr[d1] = diag_rtl[d2] = False

            dfs(idx + 1, count)

        dfs(0, 0)
        return best

    result = max_bishops(cells_per_color[0]) + max_bishops(cells_per_color[1])
    print(result)


if __name__ == "__main__":
    main()
