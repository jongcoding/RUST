#!/usr/bin/env python3
import sys, string

def main():
    s = sys.stdin.readline().rstrip("\n")
    n = len(s)
    st_trans = []
    st_link = []
    st_len = []
    st_firstpos = []
    st_occ = []
    st_trans.append({})
    st_link.append(-1)
    st_len.append(0)
    st_firstpos.append(-1)
    st_occ.append(0)
    last = 0
    for i, c in enumerate(s):
        cur = len(st_trans)
        st_trans.append({})
        st_len.append(st_len[last] + 1)
        st_firstpos.append(i)
        st_occ.append(1)
        st_link.append(0)
        p = last
        while p != -1 and c not in st_trans[p]:
            st_trans[p][c] = cur
            p = st_link[p]
        if p == -1:
            st_link[cur] = 0
        else:
            q = st_trans[p][c]
            if st_len[p] + 1 == st_len[q]:
                st_link[cur] = q
            else:
                clone = len(st_trans)
                st_trans.append(st_trans[q].copy())
                st_len.append(st_len[p] + 1)
                st_firstpos.append(st_firstpos[q])
                st_occ.append(0)
                st_link.append(st_link[q])
                while p != -1 and st_trans[p].get(c, -1) == q:
                    st_trans[p][c] = clone
                    p = st_link[p]
                st_link[q] = st_link[cur] = clone
        last = cur
    size = len(st_trans)
    order = sorted(range(size), key=lambda v: st_len[v], reverse=True)
    for v in order:
        if st_link[v] != -1:
            st_occ[st_link[v]] += st_occ[v]
    digit_freq = {d: 0 for d in "0123456789"}
    for v in range(1, size):
        cnt = st_len[v] - st_len[st_link[v]]
        occ_val = st_occ[v]
        num_str = str(occ_val)
        for ch in num_str:
            digit_freq[ch] += cnt
    letters = string.ascii_letters
    prefix = {ch: [0]*(n+1) for ch in letters}
    for i in range(n):
        for ch in letters:
            prefix[ch][i+1] = prefix[ch][i]
        if s[i] in prefix:
            prefix[s[i]][i+1] += 1
    S = {}
    for ch in letters:
        arr = prefix[ch]
        m = len(arr)
        cum = [0]*(m+1)
        s_val = 0
        for j in range(m):
            s_val += arr[j]
            cum[j+1] = s_val
        S[ch] = cum
    letter_freq = {ch: 0 for ch in letters}
    for v in range(1, size):
        L1 = st_len[st_link[v]] + 1
        L2 = st_len[v]
        cnt_subs = L2 - L1 + 1
        i = st_firstpos[v]
        A = i - L2 + 1
        B = i - L1 + 1
        if A < 0:
            A = 0
        if B < 0:
            B = 0
        for ch in letters:
            total_here = cnt_subs * prefix[ch][i+1]
            sub_here = S[ch][B+1] - S[ch][A]
            letter_freq[ch] += total_here - sub_here
    total_freq = {}
    for ch in letters:
        if letter_freq[ch]:
            total_freq[ch] = letter_freq[ch]
    for d in "0123456789":
        if digit_freq[d]:
            total_freq[d] = digit_freq[d]
    for ch in sorted(total_freq.keys(), key=lambda x: ord(x)):
        sys.stdout.write(f"{ch} {total_freq[ch]}\n")

if __name__ == '__main__':
    main()
