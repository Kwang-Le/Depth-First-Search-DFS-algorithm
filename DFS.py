n = 5
graph = [[1], [2,4],[3],[0,1],[3]]
visited = [False,False,False,False,False]
def dfs(at):
    if visited[at] == True: return
    else:
        visited[at] = True
        neighbors = graph[at]
        for i in neighbors:
            dfs(i)
start_node = 0
dfs(0)
print(visited)