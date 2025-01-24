import sys
def min_greedy(s):
    if not s:
        return 0
    z =0
    o=0
    current=s[0]
    if current=='0':
        z+=1
    else:
        o+=1
    for char in s[1:]:
        if char != current:
            if char=='0':
                z +=1
            else:
                o +=1
            current=char
    return min(z,o)

if __name__ =="__main__":
    s=sys.stdin.readline().rstrip()
    print(min_greedy(s))