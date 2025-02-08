import sys

def main():
    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    arr = [(int(data[i + 1]), i) for i in range(N)]
    
    arr.sort(key=lambda x: x[0])
    max_diff = max((original_idx - sorted_idx for sorted_idx, (_, original_idx) in enumerate(arr)), default=0)
    sys.stdout.write(str(max_diff + 1))

if __name__ == "__main__":
    main()
