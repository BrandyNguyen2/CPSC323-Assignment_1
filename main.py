# Programmers: Salvador Delgado, Brandy Nguyen, Landon Patam, & Nicholas Reeves

# Lists of Seperators, Operators and Keywords for later reference
separators = ["(", ")", ";", "{", "}", "[", "]"]
operators = ["+", "-", "*", "/", "=", "==", "<", ">", ">=", "<=", "and", "or", "not"]
keywords = ["while", "if", "for", "fi", "Integer", "Boolean", "Real", "integer", "boolean", "real", "put"]

# Takes text from input file and converts into a string with no spaces
with open("input.txt", "r" ) as file:
     input = file.read()
input_nospaces = input.replace(" ", "")
#print(input_nospaces)

# Instantiating list for Tokens
tokens = []

# Loops through the input_nospaces and seperates each token and places them into a list
temp_token = ""
    
for j in range(len(input_nospaces)):
    i = input_nospaces[j]
    if temp_token in keywords:
            tokens.append(temp_token)
            temp_token = ""
    if (i in separators) or (i in operators):         
        #index = input.index(i)
        #print(" Found special character at index: " + str(index) + " its a " + i)
        if len(temp_token) != 0:
             tokens.append(temp_token)
             temp_token = ""
        tokens.append(i)
    elif i == "\n":
         tokens.append(temp_token)
         temp_token = ""
    else:
        temp_token += i


    if j == len(input_nospaces) - 1 and temp_token:
          tokens.append(temp_token)
          temp_token = ""



# Iterates through tokens list and removes any instances of blank tokens
#print(tokens)
for i in tokens:
     if i == "" or i == " ":
          j = tokens.index(i)
          del tokens[j]
print(tokens)


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
     accepting_states = [1]
     state = 1
     for i in token:
          if state == 1:
               if i.isdigit() == True:
                    state = 1
               else:
                    state = 2

          if state == 2:
               state = 2

     if state in accepting_states:
          return True
     else:
          return False

# FSM for Real
def isReal(token):
     accepting_states = [5]
     state = 1
     for i in token:
          if state == 1:
               if i.isdigit() == True:
                    state = 2
               elif i == ".":
                    state = 3
               else:
                    state = 3

          elif state == 2:
               if i.isdigit() == True:
                    state = 2
               elif i == ".":
                    state = 4
               else:
                    state = 3

          elif state == 3:
               if i.isdigit() == True:
                    state = 3
               elif i == ".":
                    state = 3
               else:
                    state = 3

          elif state == 4:
               if i.isdigit() == True:
                    state = 5
               elif i == ".":
                    state = 3
               else:
                    state = 3

          elif state == 5:
               if i.isdigit() == True:
                    state = 5
               elif i == ".":
                    state = 3
               else:
                    state = 3
     
     if state in accepting_states:
          return True
     else:
          return False

# FSM for Identifer
def isIdentifier(token):
    accepting_states = [2]
    state = 1
    index = 0

    for char in token:
        if state == 1:
            if (char.isalpha() and (index == 0 or index == len(token)-1)):
                 state = 2
            elif (char.isalnum()):
                 state = 1
            else:
                 state = 3

        elif state == 2:
            if (char.isalpha() and (index == 0 or index == len(token)-1)):
                 state = 2
            elif (char.isalnum()):
                 state = 1
            else:
                 state = 3

        elif state == 3:
             if (char.isalpha() and (index == 0 or index == len(token)-1)):
                 state = 3
             elif (char.isalnum()):
                 state = 3
             else:
                 state = 3

        index += 1
    if state in accepting_states:
          return True
    else:
          return False
             
            
    # checks if final state is in accepting state
    if state in acceptingStates:
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
