# program to check if a string
#   is palindrome or not

# change this value for a different output
my_str = "Civic"
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
for letter in my_str.lower():
    if letter in all_letters: 
        found_letters.append(letter)
        print(found_letters)

# make it suitable for caseless comparison



# reverse the string
rev_str = reversed(found_letters)

# check if the string is equal to its reverse
print(found_letters)
if list(found_letters) == list(rev_str):
        print("yes, it is palindrome")
else:
    print("sorry but no, it is not a palindrome")




