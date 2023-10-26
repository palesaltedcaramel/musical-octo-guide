def solution(sizes):
    w, h = 0, 0
    for i, j in sizes: 
        if j > i: 
            i, j = j, i 
        w = max(i, w)
        h = max(j, h)
        
        
    return w*h
    
    
# def solution(sizes):
#     w, h = 0, 0
#     for i, j in sizes: 
#         if j > i:
#             i,j = j,i
#             if i > w: 
#                 w = i 
#             if j > h : 
#                 h = j 
#         else:
#             if i > w: 
#                 w = i 
#             if j > h : 
#                 h = j 
#     return w*h