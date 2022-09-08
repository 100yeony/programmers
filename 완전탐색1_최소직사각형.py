# sizes = [[14, 4], [19, 6], [6, 16], [18, 1100], [7, 120]]
sizes = [ [91, 50], [77, 51], [50, 1], [50, 50]]

def solution(sizes):
    x,y = 0,0
    for i in sizes:
        i.sort()
        x = max(x, i[0])
        y = max(y, i[1])
    return x*y

solution(sizes)
