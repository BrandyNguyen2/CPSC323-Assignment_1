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
#print(input_nospaces)


# List for Tokens
tokens = []

# Loops through the input_nospaces and seperates 
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

print(tokens)
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


#print("\n")
#print(tokens)

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
    if not token[0].isalpha() and not token[-1].isalpha():
     return False
    
    acceptingStates = ['VALID']
    state = 'START'
    for char in token:
        if state == 'START':
            if char.isalpha() or char == '_':
                state = 'VALID'
            else:
                state = 'INVALID'
                break
        elif state == 'VALID':
            if char.isalnum() or char == '_':
                state = 'VALID'
            else:
                state = 'INVALID'
                break
            
    # checks if final state is in accepting state
    if state in acceptingStates:
         return True
    else:
         return False





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
          elif isReal(i):
               file.write("Real                  " + i + "\n")
          elif isInteger(i):
               file.write("Integer               " + i + "\n")
          elif isIdentifier(i):
               file.write("Identifier            " + i + "\n")
          else:
               file.write("Unknwon               " + i + "\n")
