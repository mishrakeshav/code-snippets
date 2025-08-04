LOG = 20 

def dfs_binary_lifting(n, adj, root):
    up = [[-1] * LOG for i in range(n)]
    depth = [0] * n 
    stack = [(root, -1)]

    while stack:
        node, parent = stack.pop()
        up[node][0] = parent

        if parent != -1:
            depth[node] = depth[parent] + 1 
        
        for j in range(1, LOG):
            if up[node][j - 1] != -1:
                up[node][j] = up[up[node][j-1]][j - 1] # 2^(j - 1) + 2^(j - 1) = 2^j 
        
        for nbr in adj[node]:
            if nbr != parent:
                stack.append((nbr,node))
    return up, depth



def lift_node(node, k, up):

    for j in range(LOG):
        if k & (1 << j):
            node = up[node][j]
            if node == -1:
                break
    return node 
        
def find_lca(u,v,up,depth):

    if depth[u] < depth[v]:
        u,v = v, u 
    
    u = lift_node(u, depth[u] - depth[v], up)

    if u == v:
        return u 

    for j in reversed(range(LOG)):
        if up[u][j] != -1 and up[u][j] != up[v][j]:
            u = up[u][j]
            v = up[v][j]
    
    return up[u][0]
