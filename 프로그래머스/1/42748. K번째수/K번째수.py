def solution(array, commands):
    answer = []
    for _ in commands:
        i, j, k = _[0], _[1], _[2]
        sliced = array[i-1:j]
        sliced.sort()
        
        answer.append(sliced[k-1])
    return answer