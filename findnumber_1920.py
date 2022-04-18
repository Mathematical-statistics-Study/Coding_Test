"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어진다.
이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

"""
아이디어

최악의 상황은 100,000개의 배열 안에 있는 원소가 100,000개의 원소 안에 있는지 확인해야 하므로, 100,000^2번만큼 연산을 해야 할 수도 있다.
하지만, 시간 제한은 1초이므로 1초 안에 탐색을 못 할 수도 있다.
따라서, 탐색 알고리즘 중 시간 복잡도가 낮은 이진 탐색을 이용해보자. 단, 이진 탐색은 정렬된 배열 안에서만 동작한다.
"""

def iterativeBinarySearch(target, data):
    """
    반복문으로 이진 탐색을 구현해 봄
    :param target: 찾으려는 값
    :param data: 입력 데이터. 반드시 정렬되어 있어야, O(log2n)의 복잡도를 가짐
    :return:
    """
    from_index, to_index = 0, len(data) - 1
    while from_index <= to_index:
        middle_index = (from_index + to_index) // 2
        if data[middle_index] == target:
            return middle_index
        elif data[middle_index] < target:
            from_index = middle_index + 1
        else:
            to_index = middle_index - 1

    return None

import sys
N = int(sys.stdin.readline())
N_array = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
M_array = list(map(int, sys.stdin.readline().split())) #시간 제한이 1초이므로, 이진 탐색을 사용해보자! .

for i in M_array:
    return_value = iterativeBinarySearch(i, N_array)
    print(0) if return_value is None else print(1)

'''더 빠른 방법은 집합 자료형으로 찾는다
N_set = set(N_array)

for i in M_array:
    print(1) if i in N_set else print(0)
'''