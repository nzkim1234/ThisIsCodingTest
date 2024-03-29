from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n, x = map(int, input().split())
arr = list(map(int, input().split()))
count = count_by_range(arr, x, x)
if count == 0:
    print(-1)
else:
    print(count)
