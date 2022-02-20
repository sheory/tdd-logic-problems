from string import ascii_lowercase as alpha

def encrypt(statement: str) -> str:
    final_statement = generate_cipher_statement(statement, 'encrypt')

    return final_statement


def decrypt(statement: str) -> str:
    final_statement = generate_cipher_statement(statement, 'decrypt')

    return final_statement

def generate_cipher_statement(statement: str, action: str) -> str:
    final_statement = []

    for letter in statement.lower():
        final_statement.append(alpha[new_index(letter, action)])

    return ''.join(final_statement)

def new_index(letter: str, action: str) -> str:
    index = alpha.index(letter)

    if action == 'encrypt':
        return (index+3) % len(alpha)

    return (index-3) % len(alpha)