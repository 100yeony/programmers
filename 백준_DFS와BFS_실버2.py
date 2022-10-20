# graph = {}
# n = input().split()
# node, edge, start = [int(i) for i in n]
# print(node, edge, start, type(node))

# def DFS(graph, root):
#     visited = []
#     stack = [root]
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 # print('temp', graph[n], temp)
#                 temp.sort(reverse=True)
#                 stack += temp
#     return ''.join(str(i) for i in visited)


# for i in range(edge):
#     edge_info = input().split()
#     n1, n2 = [int(j) for j in edge_info]
#     # print(n1)
#     # print(n2)
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)
    
#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)

# # print(graph)
# print(DFS(graph, start))

import sys
node, edge, root = sys.stdin.readline().split()

graph = {}
for i in range(int(edge)):
    n1, n2 = input().split()
    print(n1,n2, type(n1))

    if n1 not in graph:
        graph[n1] = [n2]
    elif n1 in graph:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n2 in graph:
        graph[n2].append(n1)

# print(graph)

def DFS(graph, root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                print('graph', graph)
                temp = list(set(graph[n])-set(visited))
                print('temp', temp)




DFS(graph, root)