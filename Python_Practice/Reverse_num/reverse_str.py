# Write a Python function to reverse a given string. The function should handle any string, including those with special characters, spaces, or mixed cases.

# Example Input and Output:
# Input: "hello"
# Output: "olleh"

# Input: "Python"
# Output: "nohtyP"

# Input: "123 abc!"
# Output: "!cba 321"

def reverse_str(str):
    return str[::-1]

print(reverse_str("123 abc!"))

# ALTERNATE APPROACH USING FOR LOOP 

def reverse_string(str):
    rev = ""
    for char in str:
        rev = char + rev
    return rev

print(reverse_string("biryani12345"))