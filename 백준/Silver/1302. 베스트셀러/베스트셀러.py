N = int(input())
titles = {}
for n in range(N): 
    title = input()
    if title in titles:
        titles[title] += 1
    else: 
        titles[title] = 1 
tmp = [k for k,v in titles.items() if max(titles.values()) == v]
print(min(tmp))