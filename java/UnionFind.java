class UnionFind{
    int[] parent;
    int[] rank;
    public UnionFind(int size){
        parent = new int[size];
        for(int i = 0; i < size; i++){
            parent[i] = i;
        }
        rank = new int[size];
    }

    public int find(int x){
        if(this.parent[x] != x){
            this.parent[x] = find(parent[x]);
        }
        return this.parent[x];
    }

    public boolean union(int x, int y){
        int root_x = find(x);
        int root_y = find(y);
        if(root_x == root_y) return false;
        if(root_x != root_y){
            if(rank[root_x] > rank[root_y]){
                this.parent[root_y] = root_x;
            }else if(rank[root_x] < rank[root_y]){
                this.parent[root_x] = root_y; 
            }else{
                this.parent[root_y] = root_x;
                this.rank[root_x] += 1;
            }
        }
        return true;
    }
}