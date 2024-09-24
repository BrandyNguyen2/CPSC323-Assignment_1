# Define FSM states
START = 0
IDENTIFIER = 1
INTEGER = 2
REAL = 3
ERROR = -1

# List of operators, separators, and keywords
operators = ["+", "-", "*", "/", "=", "==", "<", ">", "<=", ">=", "and", "or", "not"]
separators = ["(", ")", ";", "{", "}", "[", "]"]
keywords = ["while", "if", "else", "fi", "for", "put", "return", "integer", "real", "boolean"]

# FSM for identifiers
def fsm_identifier(char_stream):
    state = START
    lexeme = ""
    
    for char in char_stream:
        if state == START:
            if char.isalpha():  # Identifiers must start with a letter
                state = IDENTIFIER
                lexeme += char
            else:
                return ERROR, None  # Invalid start for identifier
        
        elif state == IDENTIFIER:
            if char.isalnum():  # Continue collecting identifier characters
                lexeme += char
            else:
                break  # End of identifier
    
    return state, lexeme if state == IDENTIFIER else (ERROR, None)

# FSM for integers and real numbers
def fsm_integer_or_real(char_stream):
    state = START
    lexeme = ""
    
    for char in char_stream:
        if state == START:
            if char.isdigit():  # Start with a digit
                state = INTEGER
                lexeme += char
            else:
                return ERROR, None  # Invalid start for integer/real
        
        elif state == INTEGER:
            if char.isdigit():  # Continue reading digits
                lexeme += char
            elif char == ".":  # Transition to real number state
                state = REAL
                lexeme += char
            else:
                break  # End of integer
    
        elif state == REAL:
            if char.isdigit():  # Continue reading real number digits
                lexeme += char
            else:
                break  # End of real number

    return state, lexeme if state == INTEGER or state == REAL else (ERROR, None)

# The main lexer function
def lexer(source_code):
    i = 0
    tokens = []
    
    while i < len(source_code):
        char = source_code[i]
        
        # Skip whitespace
        if char.isspace():
            i += 1
            continue
        
        # Check for multi-character operators first (e.g., <=, >=, ==)
        if source_code[i:i+2] in operators:
            tokens.append(("operator", source_code[i:i+2]))
            i += 2
        
        # Check for single-character operators (e.g., =, <, >, +, -)
        elif char in operators:
            tokens.append(("operator", char))
            i += 1
        
        # Check for separators
        elif char in separators:
            tokens.append(("separator", char))
            i += 1
        
        # Check for keywords or identifiers
        elif char.isalpha():  # Check if it's a letter, so it could be an identifier or keyword
            token, lexeme = fsm_identifier(source_code[i:])
            if token == IDENTIFIER:
                if lexeme in keywords:
                    tokens.append(("keyword", lexeme))
                else:
                    tokens.append(("identifier", lexeme))
                i += len(lexeme)
        
        # Check for integers or real numbers
        elif char.isdigit():  # If it starts with a digit
            token, lexeme = fsm_integer_or_real(source_code[i:])
            if token == INTEGER:
                tokens.append(("integer", lexeme))
                i += len(lexeme)
            elif token == REAL:
                tokens.append(("real", lexeme))
                i += len(lexeme)
            else:
                raise ValueError(f"Unrecognized number starting at: {source_code[i]}")
        
        # Unrecognized characters
        else:
            raise ValueError(f"Unrecognized character: {char}")
    
    return tokens




# Function to print tokens and lexemes
def print_tokens(tokens):
    print("\nToken                 Lexeme")
    print("-----------------------------")
    for token, lexeme in tokens:
        print(f"{token:<20} {lexeme}")

# Main function to process the input file
def main():
    # Sample Rat24F source code (replace with file reading)
    source_code = "while (fahr <= upper) a = 23.00;"
    
    # Call the lexer to tokenize the input
    tokens = lexer(source_code)
    
    # Print the tokens and lexemes
    print_tokens(tokens)

    # Optionally, write output to a file
    with open("output.txt", "w") as file:
        file.write("Output:\nToken                 Lexeme\n")
        file.write("-----------------------------\n")
        for token, lexeme in tokens:
            file.write(f"{token:<20} {lexeme}\n")

if __name__ == "__main__":
    main()
