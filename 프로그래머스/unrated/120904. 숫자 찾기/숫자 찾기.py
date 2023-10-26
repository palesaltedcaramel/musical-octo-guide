def solution(num, k):
    num = list(map(int, str(num)))
    print(num)
    try:
        return num.index(k)+1
    except: 
        return -1