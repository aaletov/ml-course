import typing

def sort_preserving_index(
    arr: typing.List[int],
    preserve_idx: int,
) -> typing.Tuple[typing.List[int], int]:
    indexed_arr = list(enumerate(arr))
    indexed_arr.sort(key=lambda pair: pair[1])
    new_idx = -1
    for i in range(len(indexed_arr)):
        if indexed_arr[i][0] == preserve_idx:
            new_idx = i
            break

    return (list([pair[1] for pair in indexed_arr]), new_idx)

def calculate_window_bounds(
    pivot_idx: int,
    window_size: int,
    array_size: int,
) -> typing.Tuple[int, int]:
    if window_size == 1:
        return pivot_idx, pivot_idx

    left_count = pivot_idx + 1
    if left_count >= window_size:
        l_idx = pivot_idx - (window_size - 1)
        r_idx = pivot_idx
    else:
        l_idx = 0
        # take (window_size - left_count) elements to right (except pivot)
        r_idx = pivot_idx + (window_size - left_count)

    # assert l_idx >= -1
    # assert r_idx >= -1
    # assert l_idx <= (array_size - 1)
    # assert r_idx <= (array_size - 1)
    assert (r_idx - l_idx + 1) == window_size

    return l_idx, r_idx

def calculate_min_window_delta(
    arr: typing.List[int],
    window_start_left_idx: int,
    window_start_right_idx: int,
    pivot_idx: int
) -> int:
    if window_start_left_idx == window_start_right_idx:
        return 0

    # assert window_start_left_idx < (len(arr) - 1)
    # assert window_start_right_idx < (len(arr) - 1)
    assert window_start_right_idx > window_start_left_idx
    assert window_start_left_idx <= pivot_idx <= window_start_right_idx
    # consider arr is sorted

    min_delta = int(1e+10)

    # шифт по размеру окна (по меньшей границе окна)
    l_bound = pivot_idx - window_start_left_idx + 1
    r_bound = len(arr) - window_start_right_idx
    shift_count = min(l_bound, r_bound)
    if shift_count == 0:
        return arr[window_start_right_idx] - arr[window_start_left_idx]

    for shift in range(0, shift_count):
        l_idx = window_start_left_idx + shift
        r_idx = window_start_right_idx + shift
        delta = arr[r_idx] - arr[l_idx]
        if delta < min_delta:
            min_delta = delta

    return min_delta

def calculate_minimal_height_delta(
    heights: typing.List[int],
    choose_count: int,
    must_choose_idx: int,
) -> float:
    must_choose_idx -= 1
    heights, must_choose_idx = sort_preserving_index(heights, must_choose_idx)
    l_idx, r_idx = calculate_window_bounds(must_choose_idx, choose_count, len(heights))
    min_height_delta = calculate_min_window_delta(heights, l_idx, r_idx, must_choose_idx)
    return min_height_delta

def main():
    N, K, t = map(int, input().split())
    heights = list([int(input()) for i in range(N)])
    print(calculate_minimal_height_delta(heights, K, t))

if __name__ == "__main__":
    main()
