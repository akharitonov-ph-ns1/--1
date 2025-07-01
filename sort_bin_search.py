from selection import selection_sort

def sort_schedule(schedule):
    for day in schedule:
        selection_sort(schedule[day])

def binary_search(arr, goal):
    left = 0
    right = len(arr) - 1
    result = []

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == goal:
            result.append(mid)
            i = mid - 1
            while i >= 0 and arr[i] == goal:
                result.append(i)
                i -= 1
            i = mid + 1
            while i < len(arr) and arr[i] == goal:
                result.append(i)
                i += 1
            break
        elif arr[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1

    return result
