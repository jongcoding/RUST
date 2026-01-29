def solution(ineq, eq, n, m):
    answer=0
    if eq=="=":
        if eval(f"n {ineq}= m"):
            answer=1
        
    else:
        if eval(f"n {ineq} m"):
            answer=1
        
    return answer