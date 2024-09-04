class SegmentTreeRecursive:

    def __init__(self, size, arr):
        self.tree = [0] * (4 * size) # Requires 4 time if size in recursive implementation
        self.size = size
        self.arr = arr
        self.build(1, 0, size - 1)

    def build(self,node_idx, start, end):
        if start == end:
            self.tree[node_idx] = self.arr[start]
        else:
            mid = (start + end)//2
            left_node_idx, right_node_idx = 2*node_idx , 2*node_idx + 1
            self.build(left_node_idx, start, mid)
            self.build(right_node_idx, mid + 1, end)
            self.tree[node_idx] = self.tree[left_node_idx] + self.tree[right_node_idx]


    def query(self,qs,qe):
        return self.query_helper(1,0,self.size - 1, qs,qe)

    def query_helper(self, node_idx, start, end, left, right):

        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node_idx]

        left_node_idx, right_node_idx = 2*node_idx , 2*node_idx + 1
        mid = (start + end)//2
        return (self.query_helper(left_node_idx, start, mid, left, right) +
                self.query_helper(right_node_idx, mid + 1, end, left, right))

    def update(self, qs, qe, val):
        self.update_helper(1, 0, self.size - 1, qs, qe,val)

    def update_helper(self, node_idx, start, end, left, right, val):
        if left > end or right < start:
            return 0
        if (left <= start and end <= right) and (start == end):
            self.tree[node_idx] += val
        else:
            left_node_idx, right_node_idx = 2*node_idx , 2*node_idx + 1
            mid = (start + end)//2
            self.update_helper(left_node_idx, start, mid, left, right, val)
            self.update_helper(right_node_idx, mid + 1, end, left, right, val)
            self.tree[node_idx] = self.tree[left_node_idx] + self.tree[right_node_idx]


class SegmentTreeIterative:

    def __init__(self, n, data):
        self.n = n
        self.tree = [0] * (2 * n)
        self.lazy = [0] * (2 * n)  # Lazy array for range updates
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def _apply(self, pos, value, length):
        self.tree[pos] += value * length
        if pos < self.n:
            self.lazy[pos] += value

    def _push(self, pos, length):
        half = length // 2
        self._apply(pos * 2, self.lazy[pos], half)
        self._apply(pos * 2 + 1, self.lazy[pos], half)
        self.lazy[pos] = 0

    def range_update(self, left, right, value):
        # Range update by adding 'value' to all elements from 'left' to 'right'
        left += self.n
        right += self.n + 1
        left_copy, right_copy = left, right
        length = 1

        while left < right:
            if left % 2 == 1:
                self._apply(left, value, length)
                left += 1
            if right % 2 == 1:
                right -= 1
                self._apply(right, value, length)
            left //= 2
            right //= 2
            length *= 2

        left, right = left_copy, right_copy
        length = 1
        while left > 1:
            left //= 2
            right //= 2
            length *= 2
            if self.lazy[left] == 0:
                self.tree[left] = self.tree[left * 2] + self.tree[left * 2 + 1]
            if self.lazy[right] == 0 and right != left:
                self.tree[right] = self.tree[right * 2] + self.tree[right * 2 + 1]

    def query(self, left, right):
        # Range sum query from 'left' to 'right'
        left += self.n
        right += self.n + 1
        self._push(left // (left & -left), 1)
        self._push(right // (right & -right) - 1, 1)

        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2

        return result



def brut_force_sum(start,end,arr):
    res = 0
    for i in range(start, end + 1):
        res += arr[i]
    return res

def brut_force_update(start,end,arr,val):
    res = 0
    for i in range(start, end + 1):
        arr[i] += val
    return res


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    st = SegmentTreeIterative(len(arr), arr)
    print(st.tree)
    # print(st.query(0,2), brut_force_sum(0,2,arr))
    print(st.query(1, 4), brut_force_sum(1,4,arr))
    print(st.query(3, 5), brut_force_sum(3, 5, arr))
    # st.update(3,5,20)
    # brut_force_update(3,5,arr,20)
    # print(st.query(0, 2), brut_force_sum(0, 2, arr))
    # print(st.query(1, 3), brut_force_sum(1, 3, arr))
    # print(st.query(3, 5), brut_force_sum(3, 5, arr))
    # st.update(1, 3, 20)
    # brut_force_update(1, 3, arr, 20)
    # print(st.query(0, 2), brut_force_sum(0, 2, arr))
    # print(st.query(1, 3), brut_force_sum(1, 3, arr))
    # print(st.query(3, 5), brut_force_sum(3, 5, arr))
    #
    # st.update(3, 3, 20)
    # brut_force_update(3, 3, arr, 20)
    #
    # print(st.query(0, 2), brut_force_sum(0, 2, arr))
    # print(st.query(1, 3), brut_force_sum(1, 3, arr))
    # print(st.query(3, 5), brut_force_sum(3, 5, arr))








