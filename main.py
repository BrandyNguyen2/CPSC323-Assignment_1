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
    state = 'START'
    for char in token:
        if state == 'START':
            if char.isalnum() or char == '_':
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
    return state == 'VALID'



for i in tokens:
     if isReal(i) == True:
          print("\n" + str(i) + " is a real"  + "\n")
     if isInteger(i) == True:
          print("\n" + str(i) + " is an Integer" + "\n")
     if isIdentifier(i) == True:
          print("\n" + str(i) + " is an Identifier" + "\n")



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
