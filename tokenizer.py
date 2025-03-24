import chars

import parser

#%% TOKENS
class Token:
    def __init__(self, value: object = None):
        self.value: object = value
    def __repr__(self):
        return f"{type(self)}-value:{self.value}@{id(self)}"
    def __str__(self):
        return f"{type(self)} object ({self.value}) at {id(self)}"

class Break(Token):
    def __init__(self):
        super().__init__()

class Keyword(Token):
    def __init__(self):
        super().__init__()

class ExitKeyword(Keyword):
    def __init__(self):
        super().__init__()


class Literal(Token):
    def __init__(self, value):
        super().__init__()
        self.value = value

class IntLiteral(Literal):
    def __init__(self, value):
        super().__init__(value)


class Reference(Token):
    def __init__(self, value):
        super().__init__(value)

class TypeReference(Reference):
    def __init__(self, value):
        super().__init__(value)


class DeclareKeyword(Keyword):
    def __init__(self):
        super().__init__()

class Assigner(Token):
    def __init__(self):
        super().__init__()

class LetKeyword(Keyword):
    def __init__(self):
        super().__init__()

class Name(Token):
    def __init__(self, value):
        super().__init__(value)

class VariableReference(Reference):
    def __init__(self, value):
        super().__init__(value)


class ScriptLiteral(Literal):
    def __init__(self, value):
        super().__init__(value)


#%%

def tokenize(scope: str) -> list:
    tokens:    list[list[Token]] = list()
    statement: list[Token]       = list()

    scope = parser.parse(scope)[0]

    TYPES: list[str] = ["int", "script"]

    VARIABLES = []

    ichar: int = 0
    while ichar < len(scope):
        if type(scope[ichar]) == list:
            nested_tokens = tokenize(scope[ichar])
            statement.append(ScriptLiteral(nested_tokens))
            ichar += 1
        elif chars.isalpha(scope[ichar]):
            current: str = str()
            while chars.isalnum(scope[ichar]):
                current += scope[ichar]
                ichar += 1
            if current == "exit":
                statement.append(ExitKeyword())
                while chars.isspace(scope[ichar]): ichar += 1
            elif current == "declare":
                statement.append(DeclareKeyword())
                while chars.isspace(scope[ichar]): ichar += 1
                current: str = str()
                while chars.isalpha(scope[ichar]):
                    current += scope[ichar]
                    ichar += 1
                statement.append(TypeReference(current))
                while chars.isspace(scope[ichar]): ichar += 1
                current: str = str()
                while chars.isalnum(scope[ichar]):
                    current += scope[ichar]
                    ichar += 1
                statement.append(Name(current))
                VARIABLES.append(current)
            elif current == "let":
                statement.append(LetKeyword())
                while chars.isspace(scope[ichar]): ichar += 1
                current: str = str()
                while chars.isalpha(scope[ichar]):
                    current += scope[ichar]
                    ichar += 1
                statement.append(TypeReference(current))
                while chars.isspace(scope[ichar]): ichar += 1
                current: str = str()
                while chars.isalnum(scope[ichar]):
                    current += scope[ichar]
                    ichar += 1
                while scope[ichar] != '=': ichar += 1
                statement.append(Name(current))
                VARIABLES.append(current)
            elif current in TYPES:
                statement.append(TypeReference(current))
            elif current in VARIABLES:
                statement.append(VariableReference(current))
            else:
                raise RuntimeError(f"Cannot recognize symbol {current}")
        elif chars.isdigit(scope[ichar]):
            current: str = str()
            while chars.isdigit(scope[ichar]):
                current += scope[ichar]
                ichar += 1
            statement.append(IntLiteral(current))
        elif chars.isspace(scope[ichar]):
            ichar += 1
        elif scope[ichar] == ';':
            tokens.append(statement)
            statement = list()
            if ichar + 1 == len(scope):
                break
            else:
                ichar += 1
        elif scope[ichar] == '=':
            statement.append(Assigner())
            ichar += 1
        else:
            raise RuntimeError(f"Unrecognized character: {scope[ichar]}")

    return tokens