# Programmers: Salvador Delgado, Brandy Nguyen, Landon Patam, & Nicholas Reeves

# Lists of Seperators, Operators and Keywords for later reference
separators = ["(", ")", ";", "{", "}", "[", "]", ","]
operators = ["+", "-", "*", "/", "=", "==", "<", ">", ">=", "<=", "and", "or", "not"]
keywords = ["while", "if", "for", "fi", "Integer", "Boolean", "Real", "integer", "boolean", "real", "put", "function"]

# Takes text from input file and converts into a string with no spaces
with open("input.txt", "r" ) as file:
     input = file.read()
input_nospaces = input.replace(" ", "")
#print(input_nospaces)

# Instantiating list for Tokens
tokens = []

# Loops through the input_nospaces and seperates each token and places them into a list
temp_token = ""
    
for j in range(len(input)):
    i = input[j]
    if temp_token in keywords or temp_token in operators:
            tokens.append(temp_token)
            temp_token = ""
    if (i in separators) or (i in operators):         
        if len(temp_token) != 0:
          tokens.append(temp_token)
          temp_token = ""
        tokens.append(i)
    elif i == "\n":
         tokens.append(temp_token)
         temp_token = ""
    elif i == " ":
         tokens.append(temp_token)
         temp_token = ""
    else:
        temp_token += i


    if j == len(input_nospaces) - 1 and temp_token:
          tokens.append(temp_token)
          temp_token = ""



# Removes spaces and empty tokens from list
tokens = [i for i in tokens if i != "" and i != " "]

# Deals with edge cases of "<" and ">" followed by "="
index = 0
while index < len(tokens):
    i = tokens[index]

    if i == "<":
        if index + 1 < len(tokens) and tokens[index + 1] == "=":
            tokens[index] = "<="
            del tokens[index + 1]

    elif i == ">":
        if index + 1 < len(tokens) and tokens[index + 1] == "=":
            tokens[index] = ">="
            del tokens[index + 1]

    elif i == "=":
        if index + 1 < len(tokens) and tokens[index + 1] == "=":
            tokens[index] = "=="
            del tokens[index + 1]

    index += 1


# FSM for Integer
def isInteger(token):
     real_dictionary = {
     1 : [1, 2],
     2 : [2, 2]
     }

     state = 1
     accepting_states = [1]

     for i in token:
          if i.isdigit():
               state = real_dictionary[state][0]
          else:
               state = 2


         
                         
                         
               # checks if final state is in accepting state
     if state in accepting_states:
          return True
     else:
          return False
     

# FSM for Real

def isReal(token):
     real_dictionary = {
     1 : [2, 3],
     2 : [2, 4],
     3 : [3, 3],
     4 : [5, 3],
     5 : [5, 3],

     }

     state = 1
     accepting_states = [5]

     for i in token:
          if i.isdigit():
               state = real_dictionary[state][0]
          elif i == ".":
               state = real_dictionary[state][1]
          else:
               state = 3


         
                         
                         
               # checks if final state is in accepting state
     if state in accepting_states:
          return True
     else:
          return False


# FSM for Identifer
def isIdentifier(token):
     real_dictionary = {
     1 : [2, 3],
     2 : [4, 5],
     3 : [3, 3],
     4 : [4, 5],
     5 : [6, 5],
     6 : [7, 5],
     7 : [6, 5]

     }

     state = 1
     accepting_states = [2,4,6,7]

     for i in token:
          if i.isalpha():
               state = real_dictionary[state][0]
          elif i.isdigit():
               state = real_dictionary[state][1]
          else:
               state = 3
                    
                    
          # checks if final state is in accepting state
     if state in accepting_states:
          return True
     else:
          return False

def lexer(token):
     if i in operators:
          return 'Operator' 
     elif i in separators:
          return 'Separator'
     elif i in keywords:
          return 'Keyword'
     elif isReal(i):
          return 'Real'
     elif isInteger(i):
          return 'Integer'
     elif isIdentifier(i):
          return 'Identifier'
     else:
          return 'Unknown'

with open ("output.txt", "w") as file:
     file.write(f'Output:\nToken{" "*17}Lexeme\n{"-"*9}{" "*13}{"-"*8}\n')
     # Iterates through tokens list and write into output.txt file
     for i in tokens:
          # Checks if token is a seperator, operator, keyword, real, integer, or identifier
          token_type = lexer(i)
          file.write(f'{token_type:<22}{i}\n')