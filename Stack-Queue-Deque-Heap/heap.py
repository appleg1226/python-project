from sys import stdin
import heapq

def max_heap():
    N = int(stdin.readline())   # 들어갈 수의 길이

    heap = []

    for i in range(N):
        input_num = int(stdin.readline())
        heapq.heappush(heap, (-input_num, input_num))   # tuple은 (우선순위, 값) 을 받음
        print("heap 상태: ", heap)

def min_heap():
    N = int(stdin.readline())   # 들어갈 수의 길이

    heap = []

    for i in range(N):
        input_num = int(stdin.readline())
        heapq.heappush(heap, input_num)
        print("heap 상태: ", heap)



if __name__ == '__main__':
    min_heap()
