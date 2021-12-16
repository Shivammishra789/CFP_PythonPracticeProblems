from sys import argv
num = int(argv[1])
for x in range(1,num+1):
    print('2^',x,'=',pow(2,x))
