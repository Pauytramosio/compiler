import chars

class Token:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"Token({self.value})"
    def __str__(self):
        return f"Token({self.value})"
    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, Token):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)

class Expression(Token):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"Expression({self.value})"
    def __str__(self):
        return f"Expression({self.value})"
    def __eq__(self, other):
        if not isinstance(other, Expression):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, Expression):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)

class Literal(Expression):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"Literal({self.value})"
    def __str__(self):
        return f"Literal({self.value})"
    def __eq__(self, other):
        if not isinstance(other, Literal):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, Literal):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)

class IntegerLiteral(Literal):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"IntegerLiteral({self.value})"
    def __str__(self):
        return f"IntegerLiteral({self.value})"
    def __eq__(self, other):
        if not isinstance(other, IntegerLiteral):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, IntegerLiteral):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)

class StringLiteral(Literal):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"StringLiteral({self.value})"
    def __str__(self):
        return f"StringLiteral({self.value})"
    def __eq__(self, other):
        if not isinstance(other, StringLiteral):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, StringLiteral):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)


class Keyword(Token):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"Keyword({self.value})"
    def __str__(self):
        return f"Keyword({self.value})"
    def __eq__(self, other):
        if not isinstance(other, Keyword):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, Keyword):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)

class ExitKeyword(Token):
    def __init__(self, value: str):
        super().__init__(type, value)

    def __repr__(self):
        return f"ExitKeyword({self.value})"
    def __str__(self):
        return f"ExitKeyword({self.value})"
    def __eq__(self, other):
        if not isinstance(other, ExitKeyword):
            return False
        return self.value == other.value
    def __ne__(self, other):
        if not isinstance(other, ExitKeyword):
            return NotImplemented
        return self.value != other.value
    def __bool__(self):
        return bool(self.value)



class Statement:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens



def tokenize(input_string: str) -> list[Statement]:
    inpstr = input_string
    del input_string
    # to be continued hehe