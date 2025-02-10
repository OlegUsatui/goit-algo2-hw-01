def find_min_max(arr):
    def helper(left, right):
        if left == right:
            return arr[left], arr[left]

        if right - left == 1:
            return (min(arr[left], arr[right]), max(arr[left], arr[right]))

        mid = (left + right) // 2
        left_min, left_max = helper(left, mid)
        right_min, right_max = helper(mid + 1, right)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Масив не може бути порожнім")

    return helper(0, len(arr) - 1)


def quick_select(arr, k):
    if not (1 <= k <= len(arr)):
        raise ValueError("k має бути в межах довжини масиву")

    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]

        pivot_index = partition(left, right)
        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k - 1)


arr = [3, 1, 9, 7, 2, 8, 6, 5]
print(find_min_max(arr))  # Виведе (1, 9)
print(quick_select(arr, 3))  # Виведе третій найменший елемент
