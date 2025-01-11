# set a string to a variable
name = "Leo"

# print the variable
print(name)

# print an f string using the variable
print(f"Hello {name}")

# set another value to the variable
name = "Jack"

# print another f string using the new variable
print(f"Hello {name}")

# apply upper function to the variable
upper_name = name.upper()
print(upper_name)

# apply lower function to the variable
lower_name = name.lower()
print(lower_name)

# apply title function to the variable
title_name = name.title()
print(title_name)

# concat a string with the variable
print("My name is " + name)

# concat a string with the variable using f string
print(f"My name is {name}")

# set a variable with the whole sectence above
sentence = f"My name is {name}"

# print the sentence variable
print(sentence)

# split the sentence variable for each blank space in the sentence
split_sentence = sentence.split()
print(split_sentence)