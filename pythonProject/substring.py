test_str = "NANDU"

# printing original string
print("The original string is : " + str(test_str))

# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
       for j in range(i + 1, len(test_str) + 1)]

# printing result
print("All substrings of string are : " + str(res))