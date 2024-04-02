def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    build_segment_tree(arr, tree, node*2, start, mid)
    build_segment_tree(arr, tree, node*2+1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]

def update_segment_tree(arr, tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update_segment_tree(arr, tree, node*2, start, mid, index, diff)
        update_segment_tree(arr, tree, node*2+1, mid+1, end, index, diff)

def query_segment_tree(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query_segment_tree(tree, node*2, start, mid, left, right) + \
           query_segment_tree(tree, node*2+1, mid+1, end, left, right)

n, q = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (4 * (n + 1))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, p, x = query
        update_segment_tree(arr, tree, 1, 1, n, p, x)
    else:
        _, p, q = query
        print(query_segment_tree(tree, 1, 1, n, p, q))
