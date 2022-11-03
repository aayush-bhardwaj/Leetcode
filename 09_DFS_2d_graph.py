def traverse_graph(graph):
    visited = {}
    for row in range(0, len(graph)):
        for col in range(0, len(graph[0])):
            dfs(row, col, visited, graph)

    for key, value in visited.items():
        # import pdb;pdb.set_trace()
        print(graph[key[0]][key[1]])

def dfs(i, j, visited, graph):

    if (i,j) in visited:
        return

    visited[(i,j)] = True

    # row below
    if i + 1 < len(graph):
        dfs(i + 1, j , visited, graph)
    # row above
    if i - 1 >= 0:
        dfs(i - 1, j , visited, graph)
    #col left
    if j - 1 >= 0:
        dfs(i, j - 1 , visited, graph)
    # col right
    if j + 1 < len(graph[0]):
        dfs(i, j+1 , visited, graph)

    return

graph = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
traverse_graph(graph)