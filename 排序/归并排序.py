def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 找到中点
        left_half = arr[:mid]  # 分割成两个子数组
        right_half = arr[mid:]

        merge_sort(left_half)  # 递归排序左半部分
        merge_sort(right_half)  # 递归排序右半部分

        i = j = k = 0

        # 当左右两边的子数组都还有元素时，比较并合并
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 当左边子数组还有剩余时，将其添加到结果中
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 当右边子数组还有剩余时，将其添加到结果中
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 示例使用
arr = [3, 6, 8, 10, 1, 2, 1]
merge_sort(arr)
print(arr)