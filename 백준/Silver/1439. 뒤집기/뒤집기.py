s=input()

one=[o for o in s.split('0') if o !='']
zero=[o for o in s.split('1') if o !='']
print(min(len(one),len(zero)))