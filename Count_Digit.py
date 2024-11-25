# Write a Python program to count the number of digits in a given integer.

# Input Format:
# The input contains a single integer 
# 𝑛
# n, which can be positive or negative.
# Output Format:
# Print the number of digits in 
# 𝑛
# n.
# Example Input and Output:
# Example 1:

# Input: 12345
# Output: 5
# Example 2:

# Input: -9876
# Output: 4
# Example 3:

# Input: 0
# Output: 1

def Count_digit(num):
    count = 0
    rem = 0
    if (num <0):
        num = abs(num)
    while (num>0):
        rem = num % 10
        count+=1
        num = num // 10

    return count

print(Count_digit(-100))