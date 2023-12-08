T = int(input())
for tc in range(T):
    quiz = list(input())
    points_sum = 0
    points = 0 
    for i in range(1, len(quiz)+1): 
        if quiz[i-1] == 'O': 
            points += 1 
            points_sum += points
        else: 
            points = 0 
    print(points_sum)