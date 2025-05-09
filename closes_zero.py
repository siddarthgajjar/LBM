def two_sum_closest_zero(arr):

    n = len(arr)
    if n < 2:
        return []
    arr.sort()

    left, right = 0, n - 1
    closest_pair = [arr[left], arr[right]]
    min_sum = arr[left] + arr[right]

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            closest_pair = [arr[left], arr[right]]

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair


if __name__ == "__main__":
    example_input = [-8, 4, 5, -10, 3]
    output = two_sum_closest_zero(example_input)
    print(f"Input: {example_input}\n\n Output: {output}")