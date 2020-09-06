from sys import stdin

# a, b, c = map(int, stdin.readline().split())
# d = int(stdin.readline())
# a_list = list(map(int, stdin.readline().split()))

star = int(stdin.readline())

if star == 1:
    print('*')
else:
    if star % 2 == 0:
        for i in range(star*2):
            if i % 2 == 0:
                print(('* ' * (star//2)).rstrip())
            else:
                print(' *' * (star//2))
    else:
        for i in range(star * 2):
            if i % 2 == 0:
                print(('* ' * ((star+1) // 2)).rstrip())
            else:
                print(' *' * ((star-1) // 2))





"""

1
1 1 1 1 
2 1 2 1 2 1
2 2 2 2 2 2 2 2
3 2 3 2 3 2 3 2 3 2
3 3 3 3 3 3 3 3 3 3 3 3



"""
