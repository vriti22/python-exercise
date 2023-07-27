# Write a program to reverse words in a string.
# Take an input string
string = input("Enter string to be reversed: ")

# reversing words in a given string
reversed_elements_list = string.split()[::-1]
print(reversed_elements_list)
reversed_string = []
for element in reversed_elements_list:
    # appending reversed words to l
    reversed_string.append(element)
# printing reverse words
print(" ".join(reversed_string))