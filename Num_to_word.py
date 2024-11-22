# Write a Python function to convert a given number into words. The function should support numbers up to 9999.
# Example Input and Output:
# Input: 123
# Output: "one hundred twenty-three"

# Input: 45
# Output: "forty-five"

# Input: 9000
# Output: "nine thousand"

def number_to_words(num):
    if num == 0:
        return "zero"

    # Dictionaries for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    # Helper function for numbers less than 1000
    def convert_hundreds(n):
        result = ""
        if n >= 100:
            result += ones[n // 100] + " hundred"
            n %= 100
            if n > 0:
                result += " "
        if 10 < n < 20:
            result += teens[n % 10]
        else:
            if n >= 10:
                result += tens[n // 10]
                n %= 10
                if n > 0:
                    result += "-"
            if n > 0:
                result += ones[n]
        return result.strip()

    # Convert the number
    result = ""
    if num >= 1000:
        result += ones[num // 1000] + " " + thousands[1]
        num %= 1000
        if num > 0:
            result += " "
    result += convert_hundreds(num)

    return result.strip()

# Test the function
print(number_to_words(123))    # Output: "one hundred twenty-three"
print(number_to_words(45))     # Output: "forty-five"
print(number_to_words(9000))   # Output: "nine thousand"
