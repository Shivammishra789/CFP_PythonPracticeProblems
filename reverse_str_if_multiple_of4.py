string = 'shivammishra'
if len(string)%4 == 0:
    s1 = reversed(string)

    print(''.join(s1))
else:
    print(string)