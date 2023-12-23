def square_numbers(start, end):
    squared_nums = []
    sum_squared = 0
    for num in range(start, end + 1):
        squared = num ** 2
        squared_nums.append(squared)
        sum_squared += squared
    return squared_nums, sum_squared

# Example usage
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

result, total_sum = square_numbers(start_num, end_num)
print("Squared numbers:", result)
print("Sum of squared numbers:", total_sum)
