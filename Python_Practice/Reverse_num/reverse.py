# Write a Python function to reverse a given integer number. The function should handle both positive and negative numbers.

# Example Input and Output:
# Input: 123
# Output: 321

# Input: -456
# Output: -654

# Input: 1000
# Output: 1

def reverse(num):
    rev = 0 
    sign = 1
    if (num < 0):
        sign = -1
        num = - num
    while (num>0):
        rem = num%10
        rev= rev*10 + rem
        num =  num //10
    return rev * sign
    

print(reverse(-123))