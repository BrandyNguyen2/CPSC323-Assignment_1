# Programmers: Salvador Delgado, Brandy Nguyen, Landon Patam, & Nicholas Reeves

# Lists of Seperators, Operators and Keywords
separators = ["(", ")", ";", "{", "}", "[", "]"]
operators = ["+", "-", "*", "/", "=", "==", "<", ">", ">=", "<=", "and", "or", "not"]
#operators = ["<=", "=", "<", ">" ]
keywords = ["while", "if", "for", "fi", "Integer", "Boolean", "Real", "integer", "boolean", "real", "put"]

# Takes text from input file and converts into a string with no spaces
input = ""

with open("input.txt", "r" ) as file:
     input = file.read()

input_nospaces = input.replace(" ", "")


# List for Tokens
tokens = []

# Loops through the input_nospaces and seperates 
temp_token = ""
    
for i in input_nospaces:
    if temp_token in keywords:
            tokens.append(temp_token)
            temp_token = ""
    if (i in separators) or (i in operators):         
        index = input.index(i)
        #print(" Found special character at index: " + str(index) + " its a " + i)
        if len(temp_token) != 0:
             tokens.append(temp_token)
             temp_token = ""
        tokens.append(i)
    else:
        temp_token += i

# Deals with edge cases of "<" and ">" followed by "="
for i in tokens:
    index = tokens.index(i)

    if (i == "<"):
        if tokens[index + 1] == "=":
            tokens[index] = "<="
            del tokens[index + 1]
    elif (i == ">"):
         if tokens[index + 1] == "=":
            tokens[index] = ">="
            del tokens[index + 1]
    elif (i == "="):     
         if tokens[index + 1] == "=":
            tokens[index] = "=="
            del tokens[index + 1]

print("\n" + "List View" + "\n" + "=========")
print(tokens)
print("\n" + "Per Line View " + "\n" + "=============")
for i in tokens:
     print(i)
print("\n")


with open ("output.txt", "w") as file:
     file.write("Output:" + "\n" + "Token                 Lexeme" + "\n" + "---------             ----------" + "\n")
     # Iterates through tokens list and write into output.txt file
     for i in tokens:
          # Checks if token is a seperator, operator, keyword, real, integer, or identifier
          if i in operators:
               file.write("Operator              " + i + "\n") 
          elif i in separators:
               file.write("Separator             " + i + "\n")
          elif i in keywords:
               file.write("Keyword               " + i + "\n")
          elif "." in i:
               file.write("Real                  " + i + "\n")
          elif i.isdigit():
               file.write("Integer               " + i + "\n")
          else:
               file.write("Identifier            " + i + "\n")
