N=int(input())
num_list=set(map(int, input().split()))
m=int(input())
search_list=list(map(int, input().split()))
for num in search_list:
    if num in num_list:
        print(1)
    else:
        print(0)